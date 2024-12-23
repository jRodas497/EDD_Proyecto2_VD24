from src.ListaSimple.ListaSimple import ListaSimple

class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre
        self.adyacentes = ListaSimple()
        