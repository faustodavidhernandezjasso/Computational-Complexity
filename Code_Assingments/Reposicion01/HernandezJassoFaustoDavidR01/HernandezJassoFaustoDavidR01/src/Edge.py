from Vertex import Vertex

"""
    Clase para representar las aristas de una gráfica.
"""
class Edge:

    """
        Una arista está constituida por dos vértices
        y por un peso, el cual de inicio será 0.
    """
    def __init__(self, vertex1: Vertex, vertex2: Vertex):
        self.__vertex1 = vertex1
        self.__vertex2 = vertex2
        self.__weight = 0

    """
        Devolvemos el primer vértice de la arista.
    """
    @property
    def vertex1(self):
        return self.__vertex1

    """
        Devolvemos el segundo vértice de la arista.
    """
    @property
    def vertex2(self):
        return self.__vertex2

    """
        Devolvemos el peso de la arista.
    """
    @property
    def weight(self):
        return self.__weight

    """
        Establecemos el peso de la arista.
    """
    @weight.setter
    def weight(self, weight):
        if (weight < 0):
            raise ValueError("El peso debe de ser positivo")
        else:
            self.__weight = weight

    def __eq__(self, __o: object) -> bool:
        b1 = self.vertex1.element == __o.vertex1.element
        b4 = self.vertex2.element == __o.vertex2.element
        b2 = self.vertex1.element == __o.vertex2.element
        b3 = self.vertex2.element == __o.vertex1.element
        return (b1 and b4) or (b2 and b3)
        

    """
        Representación en cadena de una arista.
    """
    def __str__(self):
        msg = "("
        msg += "v" + str(self.__vertex1.element) + ", "
        msg += "v" + str(self.__vertex2.element)
        msg += ")"
        return msg