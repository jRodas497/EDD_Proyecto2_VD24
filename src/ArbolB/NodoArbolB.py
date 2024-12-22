class NodoArbolB:
    ORDEN = 5

    def __init__(self):
        self.llaves = [None] * (2 * self.ORDEN - 1)
        self.hijos = [None] * (2 * self.ORDEN)
        self.hoja = True
        self.n = 0
