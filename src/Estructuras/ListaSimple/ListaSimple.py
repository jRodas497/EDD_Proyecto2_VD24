from src.Estructuras.ListaSimple.Nodo import NodoLS

class ListaSimple:
    def __init__(self):
        self.inicio = None

    def insertar(self, nombre):
        nuevo_nodo = NodoLS(nombre)
        if self.inicio is None:
            self.inicio = nuevo_nodo
        else:
            aux = self.inicio
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo_nodo
    
    def buscar(self, nombre):
        aux = self.inicio
        while aux is not None:
            if aux.nombre == nombre:
                return aux
            aux = aux.siguiente
        return None