"""
- Complejidad Computacional
- Semestre 2023-1
- Fausto David Hernández Jasso
- 317000928
- Programa 02: Algoritmo de Aproximación
"""

import math

"""
    Clase para representar conjuntos.
"""
class Set:

    """
        Necesitamos denotar a los conjuntos con un 
        nombre para poder identificar los subconjuntos 
        de la familia que fueron elegidos para 
        la cobertura de conjutos.
    """
    def __init__(self, name:str, elements:list):
        self.__name = name
        self.__elements = frozenset(elements)

    """
        Regresamos el nombre con el cual nos referimos al conjunto.
    """
    @property
    def name(self):
        return self.__name

    """
        Regresamos los elementos del conjunto.
    """
    @property
    def elements(self):
        return self.__elements

    """
        Representación en cadena del conjunto.
    """
    def __str__(self):
        msg = "Nombre: " + self.__name + "\n"
        msg += str(set(self.__elements))
        return msg

"""
    Clase Set Cover.
"""
class SetCover:

    """
        Un ejemplar para el problema de
        Set-Covering consta de un conjunto finito 
        X y una familia de subconjuntos de X, que 
        nos referiremos a ésta como F.
    """
    def __init__(self, finite_set, family):
        if (type(finite_set) != frozenset or (not self.__verify_elements_of_family(family))):
            raise TypeError("No es correcto el ejemplar")
        self.__finite_set = finite_set
        self.__family = family
    
    """
        Regresamos al conjunto finito del ejemplar.
    """
    @property
    def finite_set(self):
        return self.__finite_set

    """
        Regresamos a la familia de subconjuntos del ejemplar.
    """
    @property
    def family(self):
        return self.__family

    """
        Verificamos que todos los elementos de la familia sean conjuntos.
    """
    def __verify_elements_of_family(self, family):
        for subset in family:
            if (type(subset.elements) != frozenset):
                return False
        return True

    """
        Representación en cadena del ejemplar.
    """
    def __str__(self):
        msg = "Ejemplar: \n"
        msg += "Conjunto finito X: \n"
        msg += str(set(self.__finite_set)) + "\n"
        msg += "Familia de subconjuntos de X: "
        for subset in self.__family:
            msg += "\n" + subset.name + " = " + str(set(subset.elements))
        return msg

    """
        Algoritmo de aproximación.
    """
    def greedy_set_cover(self):
        U = self.__finite_set
        C = set([])
        i = 0
        while U != set([]):
            S = self.select_subset_in_family(U)
            i += 1
            U = U.difference(S.elements)
            C = C.union({S.name})
        return C

    """
        Función auxiliar que será utilizada por 
        el algoritmo de aproximación.
    """
    def select_subset_in_family(self, U):
        S = Set("S", [])
        family = self.__family
        for subset in family:
            if (len(subset.elements.intersection(U)) > len(S.elements.intersection(U))):
                S = subset
        return S

    """
        Calculamos el costo de la solución.
        En el caso del problema de set-covering, el costo 
        de la solución es el número de iteraciones, hasta 
        que se da el caso del conjunto vacío.
    """    
    def cost_of_instance(self, S):
        return len(S)