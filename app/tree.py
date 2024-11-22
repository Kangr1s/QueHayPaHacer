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
terreno = Nodo("¿Qué tipo de terreno prefieres?", es_pregunta=True)
# Respuesta 2: Hijo del nodo pregunta 2
terreno_acuatico = Nodo("Acuático")
# Pregunta 3 a respuesta 2
camping = Nodo("¿Te gustaría hacer Camping?", es_pregunta=True)
# Respuesta a pregunta 3
si_camping = Nodo("Sí")

camping_robles = Nodo("Camping Los Robles")
pesca_deportiva = Nodo("Acuarius - Vía Timbío-Popayán, Los robles")
humedal = Nodo("Visita al humedal lago el Bolsón - Vereda el Lago, La Capilla, Cajibío")

no_camping = Nodo("No")
pesca_deportiva_ = Nodo("Acuarius - Vía Timbío-Popayán, Los robles")
humedal_ = Nodo("Visita al humedal lago el Bolsón - Vereda el Lago, La Capilla, Cajibío")

terreno_terrestre = Nodo("Terrestre")
armas_altura = Nodo("¿Prefieres un lugar relacionado con armas o con las alturas?", es_pregunta=True)
armas = Nodo("Armas")

gasolina = Nodo("¿Te gustaría añadir algo de gasolina?", es_pregunta=True)
si_gasolina = Nodo("Sí")
# Recomendaciones 3:
pista_carreras = Nodo("Corona Club Xtreme Park - Via Piendamo, Cajibío")
airsoft = Nodo("Lanceros Airsoft - San Bernardino, Calle 17")
campo_tiro = Nodo("Polígono la Diana pyp - Alto Puelenje")

no_gasolina = Nodo("No")
airsoft_ = Nodo("Lanceros Airsoft - San Bernardino, Calle 17")
campo_tiro_ = Nodo("Polígono la Diana pyp - Alto Puelenje")

alturas = Nodo("Alturas")
canopy = Nodo("Canopy Las Ardillas - 8 km Vía al sur, vereda La Martica")
parapente = Nodo("Parapente MTB - Vereda San Alfonso")

# armas = Nodo("¿Te gustaría algo relacionado con armas?", es_pregunta=True)
si_armas = Nodo("Sí")
# Recomendaciones 2:

# Respuesta 2: Hijo del nodo pregunta 2
no_armas = Nodo("No")

# Pregunta 3: Hijo del nodo respuesta 2
# Respuesta 3: Hijo del nodo pregunta 3
si_alturas = Nodo("Sí")
# Recomendaciones 3:

# Respuesta 3: Hijo del nodo pregunta 3
no_alturas = Nodo("No")


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
relajacion = Nodo("¿Quieres un sitio para relajarte entre actividades?", es_pregunta=True)
si_relajacion = Nodo("Sí")

mountain_bike = Nodo("Mountain bike en la Torre - Vereda El Placer")
centro_recreativo = Nodo("Centro Recreativo Pisojé de COMFACAUCA")
voley_playa = Nodo("Voley Playa - Via al Bosque")

no_relajacion = Nodo("No")
mountain_bike_ = Nodo("Mountain bike en la Torre - Vereda El Placer")
senderismo_ = Nodo("Senderismo hasta el Cerro las 3 cruces")

# Respuesta 3: Hijo del nodo pregunta 3
no_deporte = Nodo("No")
# Recomendaciones 2:
pueblo_patojo = Nodo("Visita - El Pueblito Patojo")
caminata_morro = Nodo("Caminata hasta la Pirámide El Morro de Tulcán")
senderismo = Nodo("Senderismo hasta el Cerro las 3 cruces")

# Respuesta 2: Hijo del nodo pregunta 2
urbano = Nodo("Urbano")
# Recomendaciones 2:
trampolines = Nodo("Sky Trampoline Park - Centro Comercial Monserrat Plaza")
centro_recreativo_ = Nodo("Centro Recreativo Pisojé de COMFACAUCA")


'''

Sección de creación del árbol

'''
# Crear árbol y agregar nodos
arbol = Arbol(raiz)
    
arbol.agregar_nodo(raiz, plan_extremo)
arbol.agregar_nodo(raiz, plan_fresco)
    
arbol.agregar_nodo(plan_extremo, terreno)
arbol.agregar_nodo(terreno, terreno_terrestre)
arbol.agregar_nodo(terreno_terrestre, armas_altura)
arbol.agregar_nodo(armas_altura, armas)
arbol.agregar_nodo(armas, gasolina)
arbol.agregar_nodo(gasolina, si_gasolina)
arbol.agregar_nodo(si_gasolina, pista_carreras)
arbol.agregar_nodo(si_gasolina, airsoft)
arbol.agregar_nodo(si_gasolina, campo_tiro)

arbol.agregar_nodo(gasolina, no_gasolina)
arbol.agregar_nodo(no_gasolina, airsoft_)
arbol.agregar_nodo(no_gasolina, campo_tiro_)

arbol.agregar_nodo(armas_altura, alturas)
arbol.agregar_nodo(alturas, canopy)
arbol.agregar_nodo(alturas, parapente)

arbol.agregar_nodo(terreno, terreno_acuatico)
arbol.agregar_nodo(terreno_acuatico, camping)

arbol.agregar_nodo(camping, si_camping) 
arbol.agregar_nodo(si_camping, pesca_deportiva) 
arbol.agregar_nodo(si_camping, humedal)
arbol.agregar_nodo(si_camping, camping_robles)

arbol.agregar_nodo(camping, no_camping) 
arbol.agregar_nodo(no_camping, pesca_deportiva_)
arbol.agregar_nodo(no_camping, humedal_)

arbol.agregar_nodo(plan_fresco, entorno)

arbol.agregar_nodo(entorno, natural)
arbol.agregar_nodo(natural, deporte)

arbol.agregar_nodo(deporte, si_deporte)
arbol.agregar_nodo(si_deporte, relajacion)

arbol.agregar_nodo(relajacion, si_relajacion)
arbol.agregar_nodo(si_relajacion, mountain_bike)
arbol.agregar_nodo(si_relajacion, centro_recreativo)
arbol.agregar_nodo(si_relajacion, voley_playa)

arbol.agregar_nodo(relajacion, no_relajacion)
arbol.agregar_nodo(no_relajacion, mountain_bike_)
arbol.agregar_nodo(no_relajacion, senderismo_)

arbol.agregar_nodo(deporte, no_deporte)
arbol.agregar_nodo(no_deporte, pueblo_patojo)
arbol.agregar_nodo(no_deporte, caminata_morro)
arbol.agregar_nodo(no_deporte, senderismo)

# Nivel 3 - Urbano
arbol.agregar_nodo(entorno, urbano)
arbol.agregar_nodo(urbano, trampolines)
arbol.agregar_nodo(urbano, centro_recreativo_)