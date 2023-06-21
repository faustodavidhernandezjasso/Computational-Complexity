from Vertex import Vertex
from Edge import Edge
from Graph import Graph
from MinimumSpanningTree import MinimumSpanningTree
from GraphColoring import GraphColoring
import random as r


def ejemplares_para_arbol_generador():
    """
        Ejemplares construidos para Árbol Generador de Peso Mínimo.
    """
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Ejemplar 1")
    # Ejemplo 1
    # Vértices
    v1 = Vertex(0)
    v2 = Vertex(1)
    v3 = Vertex(2)
    v4 = Vertex(3)
    v5 = Vertex(4)
    v6 = Vertex(5)
    v7 = Vertex(6)
    v8 = Vertex(7)
    v9 = Vertex(8)
    vertices = [v1, v2, v3, v4, v5, v6, v7, v8, v9]
    # Aristas
    e1 = Edge(v1, v2)
    e1.weight = 3
    v1.add_neighbor(v2)
    v2.add_neighbor(v1)
    e2 = Edge(v1, v3)
    e2.weight = 3
    v1.add_neighbor(v3)
    v3.add_neighbor(v1)
    e3 = Edge(v2, v4)
    e3.weight = 5
    v2.add_neighbor(v4)
    v4.add_neighbor(v2)
    e4 = Edge(v2, v5)
    e4.weight = 1
    v2.add_neighbor(v5)
    v5.add_neighbor(v2)
    e5 = Edge(v3, v5)
    e5.weight = 3
    v3.add_neighbor(v5)
    v5.add_neighbor(v3)
    e6 = Edge(v3, v6)
    e6.weight = 4
    v3.add_neighbor(v6)
    v6.add_neighbor(v3)
    e7 = Edge(v4, v5)
    e7.weight = 4
    v4.add_neighbor(v5)
    v5.add_neighbor(v4)
    e8 = Edge(v4, v7)
    v4.add_neighbor(v7)
    v7.add_neighbor(v4)
    e8.weight = 7
    e9 = Edge(v5, v7)
    v5.add_neighbor(v7)
    v7.add_neighbor(v5)
    e9.weight = 1
    e10 = Edge(v6, v7)
    e10.weight = 2
    v6.add_neighbor(v7)
    v7.add_neighbor(v6)
    e11 = Edge(v7, v8)
    e11.weight = 3
    v7.add_neighbor(v8)
    v8.add_neighbor(v7)
    e12 = Edge(v8, v9)
    e12.weight = 2
    v8.add_neighbor(v9)
    v9.add_neighbor(v8)
    e13 = Edge(v9, v6)
    e13.weight = 2
    v9.add_neighbor(v6)
    v6.add_neighbor(v9)
    edges = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13]
    graph1 = Graph(9, 13)
    graph1.vertices = vertices
    graph1.edges = edges
    # árbol generador de peso menor o igual a 19
    print(graph1)
    tree1 = Graph(9, 8)
    tree1.vertices = vertices
    tree1.edges = [e1, e2, e4, e7, e9, e10, e11, e12]
    ejemplar1 = MinimumSpanningTree(graph1, 19)
    b = ejemplar1.verification_phase(tree1)
    if b:
        print("Árbol Generador de Peso menor o igual a 19")
        print(tree1)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # Ejemplo 2
    # Vértices
    print("Ejemplar 2")
    u0 = Vertex(0)
    u1 = Vertex(1)
    u2 = Vertex(2)
    u3 = Vertex(3)
    u4 = Vertex(4)
    u5 = Vertex(5)
    u6 = Vertex(6)
    u7 = Vertex(7)
    u8 = Vertex(8)
    uvertices = [u0, u1, u2, u3, u4, u5, u6, u7, u8]
    # Aristas
    ue0 = Edge(u0, u1)
    ue0.weight = 1
    u0.add_neighbor(u1)
    u1.add_neighbor(u0)
    ue1 = Edge(u0, u2)
    ue1.weight = 4
    u0.add_neighbor(u2)
    u2.add_neighbor(u0)
    ue2 = Edge(u1, u2)
    ue2.weight = 2
    u1.add_neighbor(u2)
    u2.add_neighbor(u1)
    ue3 = Edge(u1, u5)
    ue3.weight = 3
    u1.add_neighbor(u5)
    u5.add_neighbor(u1)
    ue4 = Edge(u2, u3)
    ue4.weight = 6
    u2.add_neighbor(u3)
    u3.add_neighbor(u2)
    ue5 = Edge(u2, u4)
    ue5.weight = 4
    u2.add_neighbor(u4)
    u4.add_neighbor(u2)
    ue6 = Edge(u2, u5)
    ue6.weight = 1
    u2.add_neighbor(u5)
    u5.add_neighbor(u2)
    ue7 = Edge(u3, u4)
    ue7.weight = 8
    u3.add_neighbor(u4)
    u4.add_neighbor(u3)
    ue8 = Edge(u4, u5)
    ue8.weight = 9
    u4.add_neighbor(u5)
    u5.add_neighbor(u4)
    ue9 = Edge(u5, u6)
    ue9.weight = 2
    u5.add_neighbor(u6)
    u6.add_neighbor(u5)
    ue10 = Edge(u5, u7)
    ue10.weight = 5
    u5.add_neighbor(u7)
    u7.add_neighbor(u5)
    ue11 = Edge(u6, u7)
    ue11.weight = 4
    u6.add_neighbor(u7)
    u7.add_neighbor(u6)
    ue12 = Edge(u7, u8)
    ue12.weight = 5
    u7.add_neighbor(u8)
    u8.add_neighbor(u7)
    uedges = [ue0, ue1, ue2, ue3, ue4, ue5, ue6, ue7, ue8, ue9, ue10, ue11, ue12]
    graph2 = Graph(9, 13)
    graph2.vertices = uvertices
    graph2.edges = uedges
    print(graph2)
    tree2 = Graph(9, 8)
    tree2.vertices = uvertices
    tree2.edges = [ue0, ue2, ue3, ue4, ue5, ue9, ue11, ue12]
    ejemplar2 = MinimumSpanningTree(graph2, 27)
    b2 = ejemplar2.verification_phase(tree2)
    if b2:
        print("Árbol Generador con peso menor o igual a 27")
        print(tree2)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Ejemplar 3")
    # Ejemplar 3
    # Vértices 
    w0 = Vertex(0)
    w1 = Vertex(1)
    w2 = Vertex(2)
    w3 = Vertex(3)
    w4 = Vertex(4)
    w5 = Vertex(5)
    w6 = Vertex(6)
    wvertices = [w0, w1, w2, w3, w4, w5, w6]
    # Aristas
    we0 = Edge(w0, w1)
    we0.weight = 7
    w0.add_neighbor(w1)
    w1.add_neighbor(w0)
    we1 = Edge(w0, w3)
    we1.weight = 2
    w0.add_neighbor(w3)
    w3.add_neighbor(w0)
    we2 = Edge(w0, w4)
    we2.weight = 2
    w0.add_neighbor(w4)
    w4.add_neighbor(w0)
    we3 = Edge(w1, w2)
    we3.weight = 5
    w1.add_neighbor(w2)
    w2.add_neighbor(w1)
    we4 = Edge(w1, w4)
    we4.weight = 4
    w1.add_neighbor(w4)
    w4.add_neighbor(w1)
    we5 = Edge(w1, w6)
    we5.weight = 1
    w1.add_neighbor(w6)
    w6.add_neighbor(w1)
    we6 = Edge(w2, w6)
    we6.weight = 7
    w2.add_neighbor(w6)
    w6.add_neighbor(w2)
    we7 = Edge(w3, w4)
    we7.weight = 5
    w3.add_neighbor(w4)
    w4.add_neighbor(w3)
    we8 = Edge(w3, w5)
    we8.weight = 4
    w3.add_neighbor(w5)
    w5.add_neighbor(w3)
    we9 = Edge(w4, w5)
    we9.weight = 1
    w4.add_neighbor(w5)
    w5.add_neighbor(w4)
    we10 = Edge(w4, w6)
    we10.weight = 3
    w4.add_neighbor(w6)
    w6.add_neighbor(w4)
    we11 = Edge(w5, w6)
    we11.weight = 4
    w5.add_neighbor(w6)
    w6.add_neighbor(w5)
    wedges = [we0, we1, we2, we3, we4, we5, we6, we7, we8, we9, we10, we11]
    graph3 = Graph(7, 12)
    graph3.vertices = wvertices
    graph3.edges = wedges
    print(graph3)
    tree3 = Graph(7, 6)
    tree3.vertices = wvertices
    tree3.edges = [we1, we2, we3, we5, we9, we10]
    ejemplar3 = MinimumSpanningTree(graph3, 14)
    b3 = ejemplar3.verification_phase(tree3)
    if b3:
        print("Árbol Generador con peso menor o igual a 14")
        print(tree3)        
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")    


def ejemplares_construidos_de_manera_no_determinista():
    num_of_vertices = r.randint(10, 20)
    max_num_of_edges = (num_of_vertices * (num_of_vertices - 1)) // 2
    num_of_edges = r.randint(num_of_vertices, max_num_of_edges)
    graph = Graph(num_of_vertices, num_of_edges)
    for i in range(num_of_edges):
        graph.create_edge()
    k1 = r.randint(50, 80)
    instance = MinimumSpanningTree(graph, k1)
    instance.add_weights_to_graph()
    print(instance)
    k2 = r.randint(2, 10)
    inst = GraphColoring(graph, k2)
    print(inst)

"""
    Muestra el ejemplar construido de manera no-determinista,
    además que muestra los resultados producidos por la fase verificadora.
"""
if __name__ == "__main__":
    ejemplares_construidos_de_manera_no_determinista()
    # Sí se desean ver ejemplares ya construidos para árbol generador,
    # sólo basta con comentar el método de arriba y descomentar la línea siguiente.
    # ejemplares_para_arbol_generador() 