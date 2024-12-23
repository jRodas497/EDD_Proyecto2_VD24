class Viaje:
    def __init__(self, lugar_origen, lugar_destino, fecha, hora, cliente, vehiculo, ruta_tomada):
        self.lugar_origen = lugar_origen
        self.lugar_destino = lugar_destino
        self.fecha = fecha
        self.hora = hora
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.ruta = ruta_tomada
        self.costo = 0
        self.destinos = 0
        self.tiempo = 0
        
    def agregar_destino(self):
        self.destinos += 1
        
    def calcular_costo(self):
        self.costo = self.ruta_tomada.tiempo * self.vehiculo.precio_por_segundo
        return self.costo

    def mostrar_informacion(self):
        print(f"Origen: {self.lugar_origen}")
        print(f"Destino: {self.lugar_destino}")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print(f"Cliente: {self.cliente}")
        print(f"Vehículo: {self.vehiculo}")
        print(f"Ruta: {self.ruta_tomada}")
        print(f"Destinos: {self.destinos}")
        print(f"Tiempo: {self.tiempo}")
        print(f"Costo: {self.costo}")