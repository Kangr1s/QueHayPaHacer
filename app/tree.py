# Clase Nodo del Arbol
class Nodo:
    def __init__(self, dato, es_pregunta=False): # establce la pregunta como false por defecto
        self.dato = dato
        self.es_pregunta = es_pregunta
        self.primer_hijo = None
        self.siguiente_hermano = None
    
    def agregar_hijo(self, nuevo_hijo):
        if self.primer_hijo is None: # si el nodo padre no tiene hijo, se asigna el nodo nuevo como el hijo
            self.primer_hijo = nuevo_hijo
        else:
            actual = self.primer_hijo
            while actual.siguiente_hermano: # recorre hasta que actual.siguiente_hermano no sea NONE
                actual = actual.siguiente_hermano # se mueve el siguiente nodo del mismo nivel
            actual.siguiente_hermano = nuevo_hijo # asigna el nodo nuevo al nodo siguiente que fue NONE

class Arbol:
    def __init__(self, raiz):
        self.raiz = raiz

    def agregar_nodo(self, nodo_padre, nodo_hijo):
        nodo_padre.agregar_hijo(nodo_hijo) # establece un nodo padre y agrega hijos a ese nodo padre


'''

Sección de creación de nodos para el árbol

'''
# Pregunta 1: inicial
raiz = Nodo("¿Qué tipo de plan prefieres?", es_pregunta=True)

# Respuestas 1: Hijos de la pregunta inicial
plan_extremo = Nodo("plan extremo")
# Pregunta 2: Hijo del nodo plan_extremo
armas = Nodo("¿Te gustaría algo relacionado con armas?", es_pregunta=True)

# Respuesta 2: Hijo del nodo pregunta 2
si_armas = Nodo("Sí")
# Recomendaciones 2:
campo_tiro = Nodo("Polígono la Diana pyp - Alto Puelenje")
airsoft = Nodo("Lanceros Airsoft - San Bernardino, Calle 17")
# Respuesta 2: Hijo del nodo pregunta 2
no_armas = Nodo("No")

# Pregunta 3: Hijo del nodo respuesta 2
alturas = Nodo("¿Te gustaría algo relacionado con las alturas?", es_pregunta=True)
# Respuesta 3: Hijo del nodo pregunta 3
si_alturas = Nodo("Sí")
# Recomendaciones 3:
canopy = Nodo("Canopy Las Ardillas - 8 km Vía al sur, vereda La Martica")
parapente = Nodo("Parapente MTB - Vereda San Alfonso")
# Respuesta 3: Hijo del nodo pregunta 3
no_alturas = Nodo("No")
# Recomendaciones 3:
pista_carreras = Nodo("Corona Club Xtreme Park - Via Piendamo, Cajibío")

# Respuestas 1: Hijos de la pregunta inicial
plan_fresco = Nodo("plan fresco")
# Pregunta 2: Hijo del nodo plan_freco
entorno = Nodo("¿Qué entorno te gustaría?", es_pregunta=True)
# Respuesta 2: Hijo del nodo pregunta 2
natural = Nodo("Natural")
# Pregunta 3: Hijo del nodo respuesta 2
deporte = Nodo("¿Te gustaría algo relacionado con un deporte?", es_pregunta=True)
# Respuesta 3: Hijo del nodo pregunta 3
si_deporte = Nodo("Sí")
# Recomendaciones 2:
mountain_bike = Nodo("Mountain bike en la Torre - Vereda El Placer")
voley_playa = Nodo("Voley Playa - Via al Bosque")
pesca_deportiva = Nodo("Acuarius - Vía Timbío-Popayán, Los robles")
# Respuesta 3: Hijo del nodo pregunta 3
no_deporte = Nodo("No")
# Recomendaciones 2:
senderismo = Nodo("Senderismo hasta el Cerro las 3 cruces")
humedal = Nodo("Visita al humedal lago el Bolsón - Vereda el Lago, La Capilla, Cajibío")
# Respuesta 2: Hijo del nodo pregunta 2
urbano = Nodo("Urbano")
# Recomendaciones 2:
trampolines = Nodo("Sky Trampoline Park - Centro Comercial Monserrat Plaza")


'''

Sección de creación del árbol

'''
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