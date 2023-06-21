from Graph import Graph
from Vertex import Vertex
from Edge import Edge
import random as r

"""
    Clase para representar el problema de
    coloración de gráficas.
"""
class GraphColoring:

    """
        Un ejemplar genérico del problema es una gráfica no dirigida
        y un entero positivo k tal que k es menor o igual al número de
        vértices de la gráfica.
    """
    def __init__(self, graph: Graph, k: int):
        self.__graph = graph
        self.__k = k
    
    """
        Regresamos la gráfica asociada al ejemplar.
    """
    @property
    def graph(self):
        return self.__graph

    """
        Regresamos el entero positivo k asociado al ejemplar.
    """
    @property
    def k(self):
        return self.__k

    """
        Fase adivinadora.
    """
    def __guessing_phase(self):
        for vertex in self.__graph.vertices:
            vertex.color = r.randint(1, self.__k)
    
    """
        Fase verificadora.
    """
    def __verification_phase(self):
        l = len(self.__graph.vertices)
        for i in range(l):
            vertex = self.__graph.vertices[i]
            for neighbor in vertex.neighbors:
                if neighbor.color == vertex.color:
                    return False
        return True

    """
        Algoritmo no-determinístico polinomial.
    """
    def no_determinism_algorithm(self):
        self.__guessing_phase()
        return self.__verification_phase()

    """
        Representación en cadena del ejemplar genérico
        junto con la ejecución del algoritmo no-deterministíco 
        polinomial.
    """
    def __str__(self):
        s = "Ejemplar:\n"
        s += str(self.__graph)
        s += "\n"
        s += "k = " + str(self.__k)
        s += "\n"
        s += "Candidato a solución: \n"
        b = self.no_determinism_algorithm()
        for vertex in self.__graph.vertices:
            s += "Vértice: v" + str(vertex.element)
            s += "\n"
            s += "Color: " + str(vertex.color)
            s += "\n"
        if (b):
            s += "El candidato sí es una solución"
        else:
            s += "El candidato no es una solución"
        return s