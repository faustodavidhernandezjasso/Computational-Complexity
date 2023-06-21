from Graph import Graph
from Vertex import Vertex
from Edge import Edge
import random as r

"""
    Clase para representar el problema del 
    Árbol Generador de Peso Mínimo, al igual que 
    se incluye el algoritmo no-determinístico polinomial.
"""
class MinimumSpanningTree:

    """
        Un ejemplar genérico del problema es una gráfica no dirigida y con pesos en las aristas
        y un entero positivo k tal que k es menor o igual al número de
        vértices de la gráfica.
    """
    def __init__(self, graph: Graph, k: int):
        self.__graph = graph
        self.__k = k
        self.__weight = 0

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
        Les asignamos un peso a las aristas de manera no determinista,
        para terminar de construir el ejemplar genérico.
    """
    def add_weights_to_graph(self):
        for edge in self.__graph.edges:
            edge.weight = r.randint(1, 10)

    """
        Recorrido BFS sobre una gráfica no dirigida G.
    """
    def bfs(self, element, graph: Graph):
        v = Vertex(element)
        flag = False
        for vertex in graph.vertices:
            b = vertex.element == element
            if b:
                v = vertex
            flag = flag or b
        if (not flag):
            raise ValueError("El elemento no pertenece a algún vértice de la gráfica.")
        for vertex in graph.vertices:
            vertex.color = 1 # Color Rojo.
        queue = []
        v.color = 2 # Color Negro.
        queue.append(v)
        while (len(queue) != 0):
            u = queue.pop(0)
            for neighbor in u.neighbors:
                if (neighbor.color == 1):
                    neighbor.color = 2
                    queue.append(neighbor)

    """
        Verifica sí una arista dada está en la gráfica 
        que estamos tomando como ejemplar.
    """
    def __edge_is_in_graph(self, edge: Edge):
        for e in self.graph.edges:
            if e == edge:
                return True
        return False

    """
        Fase adivinadora.
    """
    def guessing_phase(self):
        n = self.graph.num_of_vertices
        tree = Graph(n, n - 1)
        while len(tree.edges) < n - 1:
            tree.create_edge()
        return tree

    """
        Fase verificadora.
    """
    def verification_phase(self, tree: Graph):
        i = r.randint(0, tree.num_of_vertices - 1)
        self.bfs(i, tree)
        is_connected = True
        for vertex in tree.vertices:
            is_connected = is_connected and (vertex.color == 2)
        if (is_connected):
            all_edges_in_original_graph = True
            for edge in tree.edges:
                all_edges_in_original_graph = all_edges_in_original_graph and (self.__edge_is_in_graph(edge))
                self.__weight += edge.weight
            if (all_edges_in_original_graph):
                return self.__weight <= self.__k
            else:
                return False
        else: 
            return False

    """
        Algoritmo no-determinístico polinomial.
    """
    def no_determinism_algorithm(self):
        tree = self.guessing_phase()
        return self.verification_phase(tree)

    """
        Representación en cadena del ejemplar genérico
        junto con la ejecución del algoritmo no-deterministíco 
        polinomial.
    """
    def __str__(self) -> str:
        s = "Ejemplar:\n"
        s += "Vértices:\n"
        s += "{"
        l = len(self.__graph.vertices)
        s += "v" + str(self.__graph.vertices[0].element)
        for i in range(1, l):
            s += ", " + "v" + str(self.__graph.vertices[i].element)
        s += "}\n"
        s += "Aristas:\n"
        l = len(self.__graph.edges)
        s += str(self.__graph.edges[0]) + " "
        s += "Peso: " + str(self.__graph.edges[0].weight)
        for i in range(1, l):
            s += ", " + str(self.__graph.edges[i]) + " "
            s += "Peso: " + str(self.__graph.edges[i].weight)
        s += "\n"
        tree = self.guessing_phase()
        s += "k = " + str(self.__k) + "\n"
        s += "Candidato a solución:\n"
        s += str(tree)
        s += "\n"
        b = self.verification_phase(tree)
        if b:
            s += "Es una solución para el ejemplar."
        else:
            s += "No es una solución para el ejemplar."
        return s