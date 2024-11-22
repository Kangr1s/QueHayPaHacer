# Clase para la creación de vertices
class Vertice:
    """Clase para representar un vértice con coordenadas y otros pesos."""
    def __init__(self, nombre, pesos=None, location=None):
        """
        Inicializa un vértice con un nombre, pesos y coordenadas opcionales.
        :param nombre: Identificador del vértice.
        :param pesos: Diccionario de atributos/pesos.
        :param location: Coordenadas como una lista [x, y].
        """
        self.nombre = nombre
        self.pesos = pesos or {}
        self.location = location  # Ejemplo: [x, y]

    def __str__(self):
        """Representación en texto del vértice."""
        coords = f"{self.location}" if self.location else "Sin coordenadas"
        return f"Vertice({self.nombre}, location: {coords}, pesos: {self.pesos})"

# Clase para la creación de las aristas
class Arista:
    """Clase para representar una conexión entre dos vértices con pesos."""
    def __init__(self, origen, destino, pesos=None):
        """
        Inicializa una arista entre dos vértices.
        :param origen: Vértice de origen.
        :param destino: Vértice de destino.
        :param pesos: Pesos asociados a la arista.
        """
        self.origen = origen
        self.destino = destino
        self.pesos = pesos or {}

    def __str__(self):
        """Representación en texto de la arista."""
        return f"Arista({self.origen.nombre} -> {self.destino.nombre}, pesos: {self.pesos})"

# Clase que utiliza a Vertices y Aristas para construir el grafo dirigido
class Grafo:
    """Clase para representar un grafo que administra vértices y aristas."""
    def __init__(self):
        self.vertices = {}  # Diccionario de vértices: {nombre: Vertice}
        self.aristas = []   # Lista de aristas: [Arista]

    def agregar_vertice(self, nombre, pesos=None, location=None):
        """
        Agrega un vértice al grafo.
        :param nombre: Nombre del vértice.
        :param pesos: Pesos del vértice como un diccionario.
        :param location: Coordenadas como una lista [x, y].
        """
        if nombre not in self.vertices:
            self.vertices[nombre] = Vertice(nombre, pesos, location)

    def agregar_arista(self, origen, destino, pesos=None):
        """
        Agrega una arista entre dos vértices.
        Si los vértices no existen, se crean automáticamente.
        :param origen: Nombre del vértice de origen.
        :param destino: Nombre del vértice de destino.
        :param pesos: Pesos asociados a la arista.
        """
        # Crear vértices si no existen
        if origen not in self.vertices:
            print(f"Creando vértice '{origen}' automáticamente.")
            self.agregar_vertice(origen)
        if destino not in self.vertices:
            print(f"Creando vértice '{destino}' automáticamente.")
            self.agregar_vertice(destino)

        # Crear y agregar la arista
        vertice_origen = self.vertices[origen]
        vertice_destino = self.vertices[destino]
        nueva_arista = Arista(vertice_origen, vertice_destino, pesos)
        self.aristas.append(nueva_arista)

    def mostrar(self):
        """Muestra todos los vértices y aristas del grafo."""
        print("Vértices:")
        for vertice in self.vertices.values():
            print(vertice)
        print("\nAristas:")
        for arista in self.aristas:
            print(arista)

# Ejemplo de uso
grafo = Grafo()

# Agregar vértices con coordenadas

#Vertices de Plan Extremo
grafo.agregar_vertice("Humedal Lago El Bolsón", {"categoría": "parque"}, location=[2.57318, -76.61129])
grafo.agregar_vertice("Lanceros Airsoft popayan", {"categoría": "historia"}, location=[2.49216, -76.58998])
grafo.agregar_vertice("Corona Club Xtreme Park", {"categoría": "compras"}, location=[2.55794, -76.56373])
grafo.agregar_vertice("Polígono la Diana pyp", {"categoría": "compras"}, location=[2.43417, -76.63542])
grafo.agregar_vertice("Parapente MTB", {"categoría": "compras"}, location=[2.42939, -76.53118])
grafo.agregar_vertice("Canopy Las Ardillas", {"categoría": "compras"}, location=[2.4286, -76.65029])
grafo.agregar_vertice("Camping Los Robles", {"categoría": "compras"}, location=[2.54002, -76.55462])
grafo.agregar_vertice("Acuarius (Restaurante, piscina, bar y Pesca deportiva)", {"categoría": "compras"}, location=[2.39853, -76.64652])

# Vertices de Plan Fresco
grafo.agregar_vertice("Centro Recreativo Pisojé de COMFACAUCA", {"categoría": "museo"}, location=[2.47688, -76.57121])
grafo.agregar_vertice("Mountain bike en La Torre", {"categoría": "compras"}, location=[2.43399, -76.55263])
grafo.agregar_vertice("Voleyb Playa - Quintas de José Miguel", {"categoría": "compras"}, location=[2.4799, -76.58856])
grafo.agregar_vertice("Pirámide El Morro de Tulcán", {"categoría": "compras"}, location=[2.44444, -76.60068])
grafo.agregar_vertice("Visita - El Pueblito Patojo", {"categoría": "compras"}, location=[2.44353, -76.59911])
grafo.agregar_vertice("Senderismo - Cerro las Tres Cruces", {"categoría": "compras"}, location=[2.44044, -76.59478])
grafo.agregar_vertice("Sky Trampoline Park", {"categoría": "compras"}, location=[2.48477, -76.58186])

# Agregar aristas
# Plan fresco
grafo.agregar_arista("Mountain bike en La Torre", "Centro Recreativo Pisojé de COMFACAUCA", {"distancia": 200})
grafo.agregar_arista("Centro Recreativo Pisojé de COMFACAUCA", "Voleyb Playa - Quintas de José Miguel", {"distancia": 200})

grafo.agregar_arista("Mountain bike en La Torre", "Senderismo - Cerro las Tres Cruces", {"distancia": 200})

grafo.agregar_arista("Visita - El Pueblito Patojo", "Pirámide El Morro de Tulcán", {"distancia": 200})
grafo.agregar_arista("Pirámide El Morro de Tulcán", "Senderismo - Cerro las Tres Cruces", {"distancia": 200})


grafo.agregar_arista("Sky Trampoline Park", "Centro Recreativo Pisojé de COMFACAUCA", {"distancia": 200})

#Plan extremo
grafo.agregar_arista("Acuarius (Restaurante, piscina, bar y Pesca deportiva)", "Humedal Lago El Bolsón", {"distancia": 200})

grafo.agregar_arista("Humedal Lago El Bolsón", "Camping Los Robles", {"distancia": 200})

grafo.agregar_arista("Canopy Las Ardillas", "Parapente MTB", {"distancia": 200})

grafo.agregar_arista("Lanceros Airsoft popayan", "Camping Los Robles", {"distancia": 200})

grafo.agregar_arista("Corona Club Xtreme Park", "Lanceros Airsoft popayan", {"distancia": 200})


# Mostrar el grafo
grafo.mostrar()