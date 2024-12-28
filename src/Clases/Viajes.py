class Viaje:
    def __init__(self, origen, destino, fecha, hora, cliente, vehiculo, ruta_tomada):
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.ruta_tomada = ruta_tomada
        self.costo = 0
        self.destinos = 0
        self.tiempo = 0
        
    def agregar_destino(self):
        self.destinos += 1
        
    def calcular_costo(self):
        self.costo = self.ruta_tomada.tiempo * self.vehiculo.precio_por_segundo
        return self.costo

    def mostrar_informacion(self):
        print(f"Origen: {self.origen}")
        print(f"Destino: {self.destino}")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print(f"Cliente: {self.cliente}")
        print(f"Vehículo: {self.vehiculo}")
        print(f"Ruta: {self.ruta_tomada}")
        print(f"Destinos: {self.destinos}")
        print(f"Tiempo: {self.tiempo}")
        print(f"Costo: {self.costo}")