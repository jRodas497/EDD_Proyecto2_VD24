class NodoArbolB:
    def __init__(self, orden):
        self.orden = orden
        self.llaves = [None] * (2 * orden - 1)
        self.hijos = [None] * (2 * orden)
        self.hoja = True
        self.n = 0