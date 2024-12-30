from src.Estructuras.ListaSimple.ListaSimple import ListaSimple
from src.Estructuras.ListaSimple.Nodo import NodoLS
from src.Estructuras.Grafo.ListaAdyacencia import ListaAdyacencia

class Viaje:
    def __init__(self, origen, destino, fecha, hora, cliente, vehiculo):
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.ruta_tomada: ListaSimple = None
        self.costo = 0
        self.destinos = 0
        self.tiempo = 0
            
    def get_ruta(self, grafo: ListaAdyacencia):
        self.ruta_tomada = grafo.obtener_rutas_desde(self.origen, self.destino)
    
    def mostrar_ruta(self):
        ruta: str = ""
        aux: NodoLS = self.ruta_tomada.inicio
        while aux is not None:
            if aux.nombre.peso_acumulado == 0:
                ruta += f"{aux.nombre.nombre}({aux.nombre.peso_acumulado}) ->" 
            else:
                ruta += f" {aux.nombre.nombre}({peso}) + {aux.nombre.peso} = {aux.nombre.peso_acumulado} ->"
            
            peso: int = aux.nombre.peso_acumulado
            aux = aux.siguiente
        
        return ruta
        
    def agregar_destino(self):
        self.destinos += 1

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