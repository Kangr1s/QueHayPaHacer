from flask import Flask, render_template, request, jsonify
from tree import arbol

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
        
        # Primero buscamos entre los hijos directos
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
                    #print(f"Encontrada respuesta en siguiente nivel: {hijo.dato}")
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
    # print(f"Respuestas recibidas: {respuestas}")
    
    nodo_actual = obtener_nodo(arbol.raiz, respuestas)
    # print(f"Nodo actual: {nodo_actual.dato}, es_pregunta: {nodo_actual.es_pregunta}")
    
    # Si el nodo actual es una respuesta y tiene una pregunta como hijo
    if not nodo_actual.es_pregunta and nodo_actual.primer_hijo and nodo_actual.primer_hijo.es_pregunta:
        siguiente_pregunta = nodo_actual.primer_hijo
        opciones = [{"respuesta": hijo.dato} for hijo in iter_nodos(siguiente_pregunta)]
        return jsonify({
            "pregunta": siguiente_pregunta.dato,
            "opciones": opciones
        })
    
    # Este metodo no sirve de nada, dado que siempre el nodo actual no va a hacer pregunta, si no, una respuesta a comparar
    # Si el nodo actual es una pregunta
    '''if nodo_actual.es_pregunta:
        opciones = [{"respuesta": hijo.dato} for hijo in iter_nodos(nodo_actual)]
        return jsonify({
            "pregunta": nodo_actual.dato,
            "opciones": opciones
        })'''
    
    # Si llegamos a una respuesta final
    # if not nodo_actual.primer_hijo:
        # return jsonify({"recomendacion": [nodo_actual.dato]})

    # Si llegamos aquí, significa que el nodo actual no tiene hijos
    # (es una respuesta final) o tiene recomendaciones
    # Si el nodo tiene hijos que son recomendaciones
    # Si el nodo tiene hijos que son recomendaciones
    recomendaciones = [hijo.dato for hijo in iter_nodos(nodo_actual)]
    return jsonify({"recomendacion": recomendaciones})

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)