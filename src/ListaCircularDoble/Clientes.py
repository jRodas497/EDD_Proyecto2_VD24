class Cliente:
    def __init__(self, dpi, nombres, apellidos, genero, telefono, direccion):
        self.dpi = dpi
        self.nombres = nombres
        self.apellidos = apellidos
        self.genero = genero
        self.telefono = telefono
        self.direccion = direccion
        self.viajes = 0
        self.siguiente = None
        self.anterior = None