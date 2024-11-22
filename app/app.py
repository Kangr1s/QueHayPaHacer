from flask import Flask, render_template, request, jsonify, url_for
from tree import arbol
from grafo import grafo  # Importar el grafo
import osmnx as ox
import networkx as nx
import folium 
from folium import DivIcon

app = Flask(__name__)

# Función de error 404. Llama la página de error
def pagina_no_encontrada(error):
    return render_template('404.html'), 404

# Ruta y función para la página principal
@app.route("/")
def index():
    # Renderizar la página principal con la primera pregunta
    return render_template("index.html", nodo = arbol.raiz)

# Método para obtener el nodo del árbol y comprarlo con lo enviado desde el POST
def obtener_nodo(nodo, respuestas):
    #print(f"Iniciando navegación desde: {nodo.dato}")
    nodo_actual = nodo
    
    for respuesta in respuestas:
        #print(f"Buscando respuesta: '{respuesta}'")
        encontrado = False
        
        #Primero buscamos entre los hijos directos
        hijo = nodo_actual.primer_hijo
        while hijo:
            if hijo.dato.lower().strip() == respuesta.lower().strip():
                #print(f"Encontrada respuesta: {hijo.dato}")
                nodo_actual = hijo
                encontrado = True
                break
            hijo = hijo.siguiente_hermano
            
        # Si no encontramos la respuesta y el nodo actual tiene una pregunta como hijo
        if not encontrado and nodo_actual.primer_hijo and nodo_actual.primer_hijo.es_pregunta:
            nodo_actual = nodo_actual.primer_hijo
            hijo = nodo_actual.primer_hijo
            while hijo:
                if hijo.dato.lower().strip() == respuesta.lower().strip():
                    print(f"Encontrada respuesta en siguiente nivel: {hijo.dato}")
                    nodo_actual = hijo
                    encontrado = True
                    break
                hijo = hijo.siguiente_hermano
                
        if not encontrado:
            #print(f"No se encontró la respuesta: {respuesta}")
            break   

    #print(f"Nodo final: {nodo_actual.dato}")
    return nodo_actual

#Itera en los nodos que están en el mismo nivel de los otros
def iter_nodos(nodo):
    actual = nodo.primer_hijo
    while actual:
        yield actual
        actual = actual.siguiente_hermano



@app.route("/pregunta", methods=["POST"])
def pregunta():
    respuestas = request.json.get("respuestas", [])
    print(f"Respuestas recibidas: {respuestas}")
    
    nodo_actual = obtener_nodo(arbol.raiz, respuestas)
    
    # Si el nodo actual es una respuesta y tiene una pregunta como hijo
    if not nodo_actual.es_pregunta and nodo_actual.primer_hijo and nodo_actual.primer_hijo.es_pregunta:
        siguiente_pregunta = nodo_actual.primer_hijo
        opciones = [{"respuesta": hijo.dato} for hijo in iter_nodos(siguiente_pregunta)]
        return jsonify({
            "pregunta": siguiente_pregunta.dato,
            "opciones": opciones
        })
    
    # Obtener recomendaciones
    recomendaciones = [hijo.dato for hijo in iter_nodos(nodo_actual)]
    
    # Definir un diccionario de traducción de rutas
    traduccion_rutas = {
        "relax-agua": ['plan extremo', 'Acuático', 'Sí'],
        "agua": ['plan extremo', 'Acuático', 'No'],
        "armas-carros": ['plan extremo', 'Terrestre', 'Armas', 'Sí'],
        "armas": ['plan extremo', 'Terrestre', 'Armas', 'No'],
        "alturas": ['plan extremo', 'Terrestre', 'Alturas'],
        "urbano": ['plan fresco', 'Urbano'],
        "relax-sport": ['plan fresco', 'Natural', 'Sí', 'Sí'],
        "sport": ['plan fresco', 'Natural', 'Sí', 'No'],
        "natural": ['plan fresco', 'Natural', 'No']
    }

    # Filtrar lugares según las respuestas y los pesos de las aristas
    # Filtrar lugares según las respuestas y los pesos de las aristas
    # Filtrar lugares según las respuestas y los pesos de las aristas
    lugares = []  # Usar una lista para mantener el orden
    for ruta, condiciones in traduccion_rutas.items():
        if respuestas == condiciones:
            print(f"Ruta encontrada: {ruta}. Buscando ubicaciones...")
            for arista in grafo.aristas:
                # Verificar si la ruta está en los pesos de la arista
                if ruta in arista.pesos.get("Ruta", []):
                    # Agregar el nodo de origen si no está ya en la lista
                    if arista.origen and not any(lugar['nombre'] == arista.origen.nombre for lugar in lugares):
                        print(f"Ubicación de origen: {arista.origen.nombre}, Coordenadas: {arista.origen.location}")
                        lugares.append({
                            "nombre": arista.origen.nombre,
                            "location": arista.origen.location
                        })
                    
                    # Agregar el nodo de destino si no está ya en la lista
                    if not any(lugar['nombre'] == arista.destino.nombre for lugar in lugares):
                        print(f"Ubicación: {arista.destino.nombre}, Coordenadas: {arista.destino.location}")
                        lugares.append({
                            "nombre": arista.destino.nombre,
                            "location": arista.destino.location
                        })
                else:
                    print(f"No se encontró la ruta '{ruta}' en los pesos de la arista hacia {arista.destino.nombre}.")

    # Crear un mapa con Folium
    mapa = folium.Map(location=[2.4489, -76.6108], zoom_start=15)  # Coordenadas de la ciudad


    for index, lugar in enumerate(lugares, start=1):  # Comenzar el índice desde 1
        # Crear el marcador con un DivIcon que incluya el icono y el número
        folium.Marker(
            location=lugar['location'],
            popup=lugar['nombre'],
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(mapa)

        # Crear un DivIcon para mostrar el número al lado del ícono
        folium.Marker(
            location=lugar['location'],
            icon=folium.DivIcon(
                icon_size=(150, 36),
                icon_anchor=(0, 0),
                html=f'<div style="font-size: 12pt; color: blue; margin-left: 20px;"><b>{index}</b></div>'
            )
        ).add_to(mapa)

    # Guardar el mapa en un archivo HTML dentro de la carpeta static
    mapa.save("app/static/maps/mapa_recomendaciones.html")

    return jsonify({
        "recomendacion": recomendaciones,
        "lugares": lugares,
        "mapa": url_for('static', filename='maps/mapa_recomendaciones.html')  # Retornar la ruta correcta del mapa
    })

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)