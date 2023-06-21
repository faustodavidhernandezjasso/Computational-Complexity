from Vertex import Vertex
from Edge import Edge
import random as r

"""
    Clase para representar una gráfica.
"""
class Graph:

    """
        Constructor.
    """
    def __init__(self, num_of_vertices: int, num_of_edges: int):
        self.__num_of_vertices = num_of_vertices
        self.__num_of_edges = num_of_edges
        self.__difference = 0
        self.__vertices = self.__create_vertices(num_of_vertices)
        self.__edges = []

    """
        Regresamos el número de vértices de la gráfica.
    """
    @property
    def num_of_vertices(self):
        return self.__num_of_vertices

    """
        Regresamos el número de aristas de la gráfica.
    """
    @property
    def num_of_edges(self):
        return self.__num_of_edges

    """
        Regresamos el conjunto de vértices de la gráfica 
        (para representar al conjunto utilizamos una lista).
    """
    @property
    def vertices(self):
        return self.__vertices

    """
        Establecemos los vértices de la gráfica.
    """
    @vertices.setter
    def vertices(self, vertices):
        self.__vertices = vertices

    """
        Regresamos el conjunto de aristas de la gráfica
        (para representar al conjunto utilizamos una lista).
    """
    @property
    def edges(self):
        return self.__edges

    """
        Establecemos las aristas de la gráfica.
    """
    @edges.setter
    def edges(self, edges):
        self.__edges = edges

    """
        Regresamos la diferencia.
    """
    @property
    def difference(self):
        return self.__difference
    
    """
        Determinamos sí entre dos vértices existe una arista.
    """
    def are_connected(self, vertex1: Vertex, vertex2: Vertex):
        if (vertex1.element == vertex2.element):
            self.__difference += 1
            return True
        else:
            boolean_one = vertex2 in vertex1.neighbors
            boolean_two = vertex1 in vertex2.neighbors
            return boolean_one and boolean_two

    """
        Creamos el conjunto de vértices de la gráfica.
    """
    def __create_vertices(self, num_of_vertices):
        vertices = []
        for i in range(num_of_vertices):
            new_vertex = Vertex(i)
            vertices.append(new_vertex)
        return vertices

    """
        Creamos una arista en la gráfica, sí está arista ya está 
        presente, no se crea nada.
    """
    def create_edge(self):
        l = len(self.__vertices) - 1
        i = r.randint(0, l)
        j = r.randint(0, l)
        self.add_edge(self.__vertices[i], self.__vertices[j])

    """
        Añadimos una arista al conjunto de aristas, sí es que 
        ésta no ha sido añadida con anterioridad.
    """
    def add_edge(self, vertex1: Vertex, vertex2: Vertex):
        if (not(self.are_connected(vertex1, vertex2))):
            vertex1.add_neighbor(vertex2)
            vertex2.add_neighbor(vertex1)
            self.__edges.append(Edge(vertex1, vertex2))

    """
        Buscamos una arista en el conjunto de aristas, 
        sí buscamos la arista entre los vértices u y v,
        buscamos tanto de la forma (u, v) como (v, u)
        ya que es la misma.
    """
    def search_edge(self, vertex1: Vertex, vertex2: Vertex):
        for e in self.__edges:
            b1 = vertex1.element == e.vertex1.element
            b2 = vertex2.element == e.vertex2.element
            b3 = vertex1.element == e.vertex2.element
            b4 = vertex2.element == e.vertex1.element
            if ((b1 and b2) or (b3 and b4)):
                return e

    """
        Representación en cadena de una gráfica.
    """
    def __str__(self) -> str:
        s = "Gráfica\n"
        s += "Vértices:\n"
        s += "{"
        lv = len(self.__vertices)
        s += "v" + str(self.__vertices[0].element)
        for i in range(1, lv):
            s += ", " + "v" + str(self.__vertices[i].element)
        s += "}\n"
        s += "Aristas:\n"
        le = len(self.__edges)
        s += "{"
        if (le != 0):
            s += str(self.__edges[0])
            for i in range(1, le):
                s += ", " + str(self.__edges[i])
        s += "}"
        return s