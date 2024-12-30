from src.Estructuras.Cola.Nodo import Nodo
from src.Clases.Vertices import Vertice

class Cola:
    def __init__(self):
        self.inicio = None
    
    def encolar(self, valor) -> None:
        nuevo_nodo = Nodo(valor)
        
        if self.vacio():
            self.inicio = nuevo_nodo
            return
        
        aux = self.inicio
        while aux.siguiente is not None:
            aux = aux.siguiente
            
        aux.siguiente = nuevo_nodo
        
    def desencolar(self):
        if self.vacio():
            return None
        
        aux = self.inicio
        self.inicio = aux.siguiente
        return aux
    
    def ordenar(self):
        if self.vacio():
            return
        
        actual = self.inicio
        while actual.siguiente is not None:
            siguiente = actual.siguiente
            while siguiente is not None:
                if actual.nombre.peso_acumulado > siguiente.nombre.peso_acumulado:
                    aux = siguiente.nombre
                    siguiente.nombre = actual.nombre
                    actual.nombre = aux
                
                actual = actual.siguiente
                
    def buscar(self, nombre) -> Nodo:
        aux: Nodo[Vertice] = self.inicio
        
        while aux is not None:
            if aux.nombre.nombre == nombre:
                return aux
            aux = aux.siguiente
            
        return None
    
    def vacio(self) -> bool:
        return self.inicio == None