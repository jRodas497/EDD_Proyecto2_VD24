from src.Estructuras.ListaSimple.ListaSimple import ListaSimple

class Vertice:
    def __init__(self, nombre, peso: int = 0, padre = None):
        self.nombre = nombre
        self.adyacentes = ListaSimple()
        self.peso = peso
        self.peso_acumulado = 0
        self.padre = padre
        
    def agregar_adyacente(self, destino, peso):
        adyacente: Vertice = Vertice(destino, peso)
        adyacente.set_peso_acumulado(peso)
        
        self.adyacentes.insertar(adyacente)
    
    def set_peso_acumulado(self, peso_acumulado):
        self.peso_acumulado += peso_acumulado
        