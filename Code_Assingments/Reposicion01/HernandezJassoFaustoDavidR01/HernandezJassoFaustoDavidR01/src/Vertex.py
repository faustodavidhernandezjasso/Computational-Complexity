"""
    Clase para representar vértices de una gráfica.
"""
class Vertex:

    """
        Un vértice está constituido por el elemento de ese vértice,
        un color (que de inicio será el color 0) y una lista 
        de vecinos.
    """
    def __init__(self, element):
        self.__element = element
        self.__color = 0
        self.__neighbors = list()

    """
        Devolvemos el elemento del vértice.
    """
    @property
    def element(self):
        return self.__element

    """
        Establecemos el elemento del vértice.
    """
    @element.setter
    def element(self, element):
        self.__element = element
    
    """
        Devolvemos el color del vértice.
    """
    @property
    def color(self):
        return self.__color

    """
        Establecemos el color del vértice.
    """
    @color.setter
    def color(self, color):
        if (color <= 0):
            raise ValueError("Los colores de los vértices deben de ser identificados con enteros positivos")
        self.__color = color

    """
        Devolvemos los vecinos del vértice.
    """
    @property
    def neighbors(self):
        return self.__neighbors
    
    """
        Añadimos un vecino a la lista de vecinos del vértice.
    """
    def add_neighbor(self, neighbor):
        self.__neighbors.append(neighbor)

    """
        Regresamos el grado del vértice.
    """
    def get_degree(self):
        return len(self.__neighbors)

    """
        Representación en cadena de un vértice.
    """
    def __str__(self):
        msg = "Elemento: " + str(self.__element) + " "
        l = len(self.__neighbors)
        msg += "Vecinos: {"
        if (l != 0):
            msg += str(self.__neighbors[0].element)
            for i in range(1, l):
                msg += ", " + str(self.__neighbors[i].element)
        msg += "}"
        return msg