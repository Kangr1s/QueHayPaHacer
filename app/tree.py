# app/arbol.py
class Nodo:
    def __init__(self, dato, es_pregunta=False):
        self.dato = dato
        self.es_pregunta = es_pregunta
        self.primer_hijo = None
        self.siguiente_hermano = None
    
    def agregar_hijo(self, nuevo_hijo):
        if self.primer_hijo is None:
            self.primer_hijo = nuevo_hijo
        else:
            actual = self.primer_hijo
            while actual.siguiente_hermano:
                actual = actual.siguiente_hermano
            actual.siguiente_hermano = nuevo_hijo

class Arbol:
    def __init__(self, raiz):
        self.raiz = raiz

    def agregar_nodo(self, nodo_padre, nodo_hijo):
        nodo_padre.agregar_hijo(nodo_hijo)

# Crear nodos - Preguntas
raiz = Nodo("¿Qué tipo de plan prefieres?", es_pregunta=True)
# Crear nodos - Respuestas y recomendaciones
plan_extremo = Nodo("plan extremo", es_pregunta=False)
plan_fresco = Nodo("plan fresco", es_pregunta=False)

armas = Nodo("¿Te gustaría algo relacionado con armas?", es_pregunta=True)

si_armas = Nodo("Sí", es_pregunta=False)
campo_tiro = Nodo("Polígono la Diana pyp - Alto Puelenje ", es_pregunta=False)
airsoft = Nodo("Lanceros Airsoft - San Bernardino, Calle 17", es_pregunta=False)

no_armas = Nodo("No", es_pregunta=False)
alturas = Nodo("¿Te gustaría algo relacionado con las alturas?", es_pregunta=True)

si_alturas = Nodo("Sí", es_pregunta=False)
canopy = Nodo("Canopy Las Ardillas - 8 km Vía al sur, vereda La Martica ", es_pregunta=False)
parapente = Nodo("Parapente MTB - Vereda San Alfonso", es_pregunta=False)

no_alturas = Nodo("No", es_pregunta=False)
pista_carreras = Nodo("Corona Club Xtreme Park - Via Piendamo, Cajibío", es_pregunta=False)

entorno = Nodo("¿Qué entorno te gustaría?", es_pregunta=True)
natural = Nodo("Natural", es_pregunta=False)

deporte = Nodo("¿Te gustaría algo relacionado con un deporte?", es_pregunta=True)
si_deporte = Nodo("Sí", es_pregunta=False)
mountain_bike = Nodo("Mountain bike en la Torre - Vereda El Placer", es_pregunta=False)
voley_playa = Nodo("Voley Playa - Via al Bosque", es_pregunta=False)
pesca_deportiva = Nodo("Acuarius - Vía Timbío-Popayán, Los robles", es_pregunta=False)

no_deporte = Nodo("No", es_pregunta=False)
senderismo = Nodo("Senderismo hasta el Cerro las 3 cruces", es_pregunta=False)
humedal = Nodo("Visita al humedal lago el Bolsón - Vereda el Lago, La Capilla, Cajibío ", es_pregunta=False)
urbano = Nodo("Urbano", es_pregunta=False)
trampolines = Nodo("Sky Trampoline Park - Centro Comercial Monserrat Plaza", es_pregunta=False)

# Crear árbol y agregar nodos
arbol = Arbol(raiz)
    
arbol.agregar_nodo(raiz, plan_extremo)
arbol.agregar_nodo(raiz, plan_fresco)
    
arbol.agregar_nodo(plan_extremo, armas)
arbol.agregar_nodo(armas, si_armas)
arbol.agregar_nodo(si_armas, campo_tiro)
arbol.agregar_nodo(si_armas, airsoft)
arbol.agregar_nodo(armas, no_armas)
    
arbol.agregar_nodo(no_armas, alturas)
arbol.agregar_nodo(alturas, si_alturas)
arbol.agregar_nodo(si_alturas, canopy)
arbol.agregar_nodo(si_alturas, parapente)
arbol.agregar_nodo(alturas, no_alturas)
arbol.agregar_nodo(no_alturas, pista_carreras)
    
arbol.agregar_nodo(plan_fresco, entorno)
arbol.agregar_nodo(entorno, natural)
arbol.agregar_nodo(natural, deporte)
arbol.agregar_nodo(deporte, si_deporte)
arbol.agregar_nodo(si_deporte, mountain_bike)
arbol.agregar_nodo(si_deporte, voley_playa)
arbol.agregar_nodo(si_deporte, pesca_deportiva)
arbol.agregar_nodo(deporte, no_deporte)
arbol.agregar_nodo(no_deporte, senderismo)
arbol.agregar_nodo(no_deporte, humedal)
    
arbol.agregar_nodo(entorno, urbano)
arbol.agregar_nodo(urbano, trampolines)