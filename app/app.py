from flask import Flask, render_template, url_for, redirect, request, jsonify
from tree import arbol, Nodo

app = Flask(__name__)

def pagina_no_encontrada(error):
    return render_template('404.html'), 404
    # return redirect(url_for('index')) # Redirecciona a la página index dado el error 404


# Función para encontrar el nodo con base en las respuestas
def obtener_nodo(nodo, respuestas):
    for respuesta in respuestas:
        for hijo in nodo.hijos:
            if hijo.pregunta == respuesta:
                nodo = hijo
                break
    return nodo

@app.route("/")
def index():
    # Renderizar la página principal con la primera pregunta
    return render_template("index.html", nodo=arbol.raiz)

@app.route("/pregunta", methods=["POST"])
def pregunta():
    respuestas = request.json.get("respuestas", [])
    nodo_actual = obtener_nodo(arbol.raiz, respuestas)
    
    # Si es un nodo final, devolver todas las recomendaciones (hijos)
    if not nodo_actual.hijos:
        return jsonify({"recomendacion": [nodo_actual.pregunta]})
    
    # Revisar si los hijos son recomendaciones finales
    if all(not hijo.hijos for hijo in nodo_actual.hijos):
        recomendaciones = [hijo.pregunta for hijo in nodo_actual.hijos]
        return jsonify({"recomendacion": recomendaciones})

    # Devolver pregunta y opciones para el nodo actual si no es nodo final
    opciones = [{"respuesta": hijo.pregunta} for hijo in nodo_actual.hijos]
    return jsonify({"pregunta": nodo_actual.pregunta, "opciones": opciones})

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug = True, port = 5000)