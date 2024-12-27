class Ruta:
    def __init__(self, origen, destino, tiempo):
        self.origen = origen
        self.destino = destino
        self.tiempo = tiempo
        
    def __str__(self):
        return f"{self.origen} -> {self.destino} ({self.tiempo} min)"