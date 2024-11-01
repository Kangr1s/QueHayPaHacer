# app/arbol.py

class Nodo:
    def __init__(self, pregunta, respuesta=None):
        self.pregunta = pregunta     # Pregunta o descripción del nodo
        self.respuesta = respuesta   # Respuesta o valor en este nodo (opcional)
        self.hijos = []              # Lista de hijos del nodo

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

    def __repr__(self, nivel=0):
        ret = "\t" * nivel + f"{self.pregunta}: {self.respuesta if self.respuesta else ''}\n"
        for hijo in self.hijos:
            ret += hijo.__repr__(nivel + 1)
        return ret

class Arbol:
    def __init__(self, raiz):
        self.raiz = raiz

    def imprimir_arbol(self):
        if self.raiz is not None:
            print(self.raiz)

# Crear el árbol con la estructura deseada

# Raíz del árbol
raiz = Nodo("¿Qué tipo de plan prefieres?")

# Nodos principales
plan_extremo = Nodo("plan extremo")
plan_fresco = Nodo("plan fresco")

# Agregar los planes principales al nodo raíz
raiz.agregar_hijo(plan_extremo)
raiz.agregar_hijo(plan_fresco)

# Nodos para "plan extremo"
armas = Nodo("¿Te gustaría algo relacionado con armas?")
armas_si = Nodo("Sí")
armas_no = Nodo("No")

# Nodos hijos de "Sí" y "No" bajo "¿Te gustaría algo relacionado con armas?"
armas_si.agregar_hijo(Nodo("Campo de tiro"))
armas_si.agregar_hijo(Nodo("Airsoft"))

alturas = Nodo("¿Te gustaría algo relacionado con las alturas?")
alturas_si = Nodo("Sí")
alturas_no = Nodo("No")

alturas_si.agregar_hijo(Nodo("Canopy"))
alturas_si.agregar_hijo(Nodo("Parapente"))
alturas_no.agregar_hijo(Nodo("Pista de carreras"))

# Armar el subárbol de "plan extremo"
plan_extremo.agregar_hijo(armas)
armas.agregar_hijo(armas_si)
armas.agregar_hijo(armas_no)
armas_no.agregar_hijo(alturas)
alturas.agregar_hijo(alturas_si)
alturas.agregar_hijo(alturas_no)

# Nodos para "plan fresco"
entorno = Nodo("¿Qué entorno te gustaría?")
natural = Nodo("Natural")
urbano = Nodo("Urbano")

# Subárbol para "Natural"
deporte = Nodo("¿Te gustaría algo relacionado con un deporte?")
deporte_si = Nodo("Sí")
deporte_no = Nodo("No")

deporte_si.agregar_hijo(Nodo("Mountain bike en la Torre"))
deporte_si.agregar_hijo(Nodo("Voley Playa"))
deporte_si.agregar_hijo(Nodo("Pesca Deportiva"))
deporte_no.agregar_hijo(Nodo("Senderismo hasta las 3 cruces"))
deporte_no.agregar_hijo(Nodo("Visita al humedal lago el Bolsón"))

# Subárbol para "Urbano"
urbano.agregar_hijo(Nodo("Parque de trampolines"))

# Armar el subárbol de "plan fresco"
plan_fresco.agregar_hijo(entorno)
entorno.agregar_hijo(natural)
entorno.agregar_hijo(urbano)
natural.agregar_hijo(deporte)
deporte.agregar_hijo(deporte_si)
deporte.agregar_hijo(deporte_no)

# Crear el árbol
arbol = Arbol(raiz)