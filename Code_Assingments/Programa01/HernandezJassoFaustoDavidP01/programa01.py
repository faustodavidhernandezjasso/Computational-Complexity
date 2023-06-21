"""
    Complejidad Computacional
    Semestre 2023-1
    Programa 01
    Profesora: María de Luz Gasca Soto
    Ayudante: José Luis Vázquez Lázaro
    Fausto David Hernández Jasso
    317000928
"""

import random as rand
import numpy as np


"""
    Alcanzabilidad.
    Dada una gráfica no dirigida G = (V, E), con
    dos vértices distinguidos s y t. ¿Existe un
    camino que no repite vértices de s a t en G?
"""

class Alcanzabilidad:

    """
        Constructor.
    """
    def __init__(self):
        self.numero_de_vertices = rand.randint(10,20)
        self.grafica = self.__crea_grafica()


    """
        Creamos la gráfica de manera aleatoria.
        La representación de la gráfica se hará por medio de una matriz de adyacencias.
        Está inicializada en 0 todas las entradas de la matriz.
    """
    def __crea_grafica(self):
        grafica = np.zeros((self.numero_de_vertices, self.numero_de_vertices), dtype=int)
        for i in range(self.numero_de_vertices):
            self.__agrega_arista(grafica)
        return grafica


    """
        Agregamos aristas de manera no determinista. Al ser una gráfica no dirigida 
        siempre debemos de garantizar lo siguiente:
        El vértice v es vecino del vértice u sí y sólo sí u es vértice de v.
    """
    def __agrega_arista(self, grafica):
        numero_de_aristas = rand.randint(1, self.numero_de_vertices)
        for i in range(numero_de_aristas):
            v = rand.randint(0, self.numero_de_vertices - 1)
            u = rand.randint(0, self.numero_de_vertices - 1)
            if (u == v):
                grafica[u][v] = 0
                grafica[v][u] = 0
            else:
                grafica[u][v] = 1
                grafica[v][u] = 1

    
    """
        Obtenemos la lista de vecinos de algún vértice de la gráfica G.
    """
    def __get_vecinos(self, i):
        vecinos = []
        for j in range(self.numero_de_vertices):
            if (self.grafica[i][j] == 1):
                vecinos.append(j + 1)
        return vecinos


    """
        De manera no determinista, proponemos un caminos desde el vértice s hacia el vértice t.
    """
    def __generar_un_camino(self, s, t):
        camino = [s]
        l = rand.randint(1, self.numero_de_vertices)
        for i in range(l):
            j = rand.randint(1, self.numero_de_vertices)
            if j in camino:
                continue
            else:
                camino.append(j)
        return camino


    """
        Dado un camino, determinamos sí es que éste existe en la gráfica G.
    """
    def __existe_camino(self, camino):
        l = len(camino) - 1
        existencia = True
        for i in range(l):
            if (self.grafica[camino[i] - 1][camino[i + 1] - 1] == 1):
                existencia = existencia and (True)
            else:
                return False
        return existencia
            

    """
        Mostramos el ejemplar generado.
    """
    def muestra_ejemplar(self):
        for i in range(self.numero_de_vertices):
            print("Vértice " + str(i + 1))
            vecinos = self.__get_vecinos(i)
            print("Vecinos: " + str(vecinos))
        s = rand.randint(1, self.numero_de_vertices)
        t = rand.randint(1, self.numero_de_vertices)
        while (s == t):
            t = rand.randint(1, self.numero_de_vertices)
        print("Determinaremos sí existe un camino del vértice " + str(s) + " al vértice " + str(t) + ".")
        print("Generando lista de vértices...")
        camino = self.__generar_un_camino(s, t)
        print("Camino candidato: " + str(camino))
        if (self.__existe_camino(camino)):
            print("El candidato " + str(camino) + " sí es solución al problema")
        else:
            print("El candidato " + str(camino) + " no es solución al problema")


"""
    Clase Variable.
    Representamos a una variable que forma parte 
    de una cláusula en Forma Normal Conjuntiva.
"""
class Variable:


    """
        Constructor.
        Una variable tiene nombre y estado.
        Adicionalmente, decidí optar porque tuviera un parámetro 
        extra el cuál nos dice sí la variable es una negación, ésto 
        es necesario para la representación en cadena de la variable.
    """
    def __init__(self, nombre : str, esNegada: bool, estado = True):
        self.__nombre = nombre
        self.__esNegada = esNegada
        self.__estado = estado


    """
        El nombre de la variable.
    """
    @property
    def nombre(self):
        return self.__nombre


    """
        Nos indica sí la variable está negada.
    """
    @property
    def esNegada(self):
        return self.__esNegada


    """
        Returns sí la variable está negada.
    """
    @esNegada.setter
    def esNegada(self, esNegada):
        self.__esNegada = esNegada


    """
        Returns el estado de la variable.
    """
    @property
    def estado(self):
        return self.__estado


    """
        Actualizamos el estado de la variable.
    """
    @estado.setter
    def estado(self, estado):
        self.__estado = estado


    """
        Determinamos sí una variable es igual a otra.
    """
    def __eq__(self, variable):
        if ((variable == None) or (type(self) != type(variable))):
            return False
        return (self.__nombre == variable.nombre) and (self.esNegada == variable.esNegada)


    """
        Representación en cadena de la variable.
    """
    def __str__(self) -> str:
        if (self.__esNegada):
            return "~" + self.nombre
        else:
            return self.nombre


"""
    Cláusulas que forman parte 
    de una expresión en Forma Normal Conjuntiva.
"""
class Clausula:


    """
        Constructor.
        Generamos la cláusula, escogemos de manera no determinista las 
        variables que formarán parte de la cláusula. Hacemos la observación
        que ésta cláusula siempre tiene 3 variables.
    """
    def __init__(self, variables):
        self.__clausula = self.__crea_clausula(variables)


    """
        Returns la cláusula.
    """
    @property
    def clausula(self):
        return self.__clausula


    """
        Creamos la cláusula de manera no determinista.
    """
    def __crea_clausula(self, variables):
        clausula = []
        for i in range(3):
            j = rand.randint(0, 9)
            negada = rand.randint(0, 1)
            if (negada == 1):
                clausula.append(Variable(variables[j].nombre, True))
            else:
                clausula.append(variables[j])
        return clausula


    """
        Representación en cadena de la cláusula.
    """
    def __str__(self) -> str:
        s = "( "
        for i in range(3):
            s += self.__clausula[i].__str__()
            if (i != 2):
                s += " || "
        return s + " )"


"""
    3-SAT.
    Dada una expresión lógica en Forma Normal Conjuntiva. 
    Determinamos sí dicha expresión es satisfacible.
"""
class ThreeSAT:


    # Variables
    vars = ["u", "v", "w", "x", "y", "z", "a", "b", "c", "d"]


    """
        Constructor.
    """
    def __init__(self):
        self.variables = self.__crea_variables()
        self.expresion = self.__crea_expresion()


    """
        Creamos las variables que formarán parte de la expresión.
    """
    def __crea_variables(self):
        lista_de_variables = []
        for var in self.vars:
            variable = Variable(var, False)
            lista_de_variables.append(variable)
        return lista_de_variables

    
    """
        Creamos la expresión.
    """
    def __crea_expresion(self):
        expresion = []
        for i in range(5):
            clausula = Clausula(self.variables)
            expresion.append(clausula)
        return expresion


    """
        Representación en cadena de la expresión.
    """
    def __str__(self) -> str:
        s = ""
        for i in range(5):
            s += self.expresion[i].__str__()
            if (i != 4):
                s += " & "
        return s

    
    """
        De manera no determinista asignamos los estados a 
        las variables que forman parte de la expresión que ya 
        hemos generado.
    """
    def __asigna_estados(self):
        vars = set()
        for i in range(5):
            for variable in self.expresion[i].clausula:
                vars.add(variable.nombre)
        for var in vars:
            self.__busca_variable_y_asigna_estado(var)

    
    """
        Evaluamos la expresión para determinar sí es satisfacible 
        bajo los estados de las variables que la conforman.
    """
    def __evalua_expresion(self):
        clausulas = []
        for i in range(5):
            resultado = False
            for variable in self.expresion[i].clausula:
                resultado = resultado or (variable.estado)
            clausulas.append(resultado)
        resultado = True
        for i in range(5):
            resultado = resultado and (clausulas[i])
        return resultado


    """
        Función auxiliar para poder asignar los estados a las 
        variable de las cláusulas.
    """
    def __busca_variable_y_asigna_estado(self, var):
        estado = rand.randint(0, 1)
        for i in range(5):
            for variable in self.expresion[i].clausula:
                if ((variable.nombre == var) and (variable.esNegada)):
                    variable.estado = self.__asigna_estado(1 - estado)
                elif ((variable.nombre == var) and (not (variable.esNegada))):
                    variable.estado = self.__asigna_estado(estado)
                else:
                    pass
        
    
    """
        Asiganamos un estado a una variable dada.
    """
    def __asigna_estado(self, estado):
        if (estado == 0):
            return False
        else:
            return True


    """
        Mostramos el ejemplar que hemos generado.
    """
    def muestra_ejemplar(self):
        msg = "Expresión\n" 
        msg += str(self) + "\n"
        self.__asigna_estados()
        msg += "Asignación de estados de las variables: \n"
        for i in range(5):
            for variable in self.expresion[i].clausula:
                msg += "Variable: " + str(variable)
                msg += " "
                msg += "Estado: " + str(variable.estado)
                msg += "\n"
        print("Evaluando la expresión con la asignación de estados")
        resultado = self.__evalua_expresion()
        if (resultado):
            msg += "La expresión sí se satisface dado el conjunto de estados de las variables." 
        else:
            msg += "La expresión no se satisface dado el conjunto de estados de las variables."
        print(msg)


if __name__ == "__main__":
    msg = "Hola, ¿Qué algoritmo deseas probar?"
    msg += "\n"
    msg += "1. Alcanzabilidad. \n"
    msg += "2. 3-SAT. \n"
    msg += "3. Salir. \n"
    ip = input(msg)
    try:
        r = int(ip)
        if (r == 1):
            ejemplar = Alcanzabilidad()
            ejemplar.muestra_ejemplar()
        elif (r == 2):
            ejemplar = ThreeSAT()
            ejemplar.muestra_ejemplar()
        else:
            print("Nos vemos pronto.")
    except ValueError:
        print("Introduce una opción válida")