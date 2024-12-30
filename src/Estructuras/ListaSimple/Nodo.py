class NodoLS:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

    def __str__(self):
        return str(self.nombre)