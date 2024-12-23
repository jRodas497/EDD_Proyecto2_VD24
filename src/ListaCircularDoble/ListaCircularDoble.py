from src.Clases.Clientes import Cliente

class ListaCircularDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar(self, cliente):
        if self.primero is None:
            self.primero = self.ultimo = cliente
            self.primero.siguiente = self.primero.anterior = self.primero
        else:
            actual = self.primero
            while actual.siguiente != self.primero and int(actual.dpi) < int(cliente.dpi):
                actual = actual.siguiente
            if actual == self.primero and int(cliente.dpi) < int(actual.dpi):
                cliente.siguiente = self.primero
                cliente.anterior = self.ultimo
                self.primero.anterior = cliente
                self.ultimo.siguiente = cliente
                self.primero = cliente
            elif actual == self.ultimo and int(cliente.dpi) > int(actual.dpi):
                cliente.siguiente = self.primero
                cliente.anterior = self.ultimo
                self.ultimo.siguiente = cliente
                self.primero.anterior = cliente
                self.ultimo = cliente
            else:
                cliente.siguiente = actual
                cliente.anterior = actual.anterior
                actual.anterior.siguiente = cliente
                actual.anterior = cliente
                
    def existe_dpi(self, dpi):
        actual = self.primero
        if actual is None:
            return False
        while True:
            if actual.dpi == dpi:
                return True
            actual = actual.siguiente
            if actual == self.primero:
                break
        return False
                    
    def modificar(self, dpi, nuevos_datos):
        if not self.existe_dpi(dpi):
            print(f"Cliente con DPI {dpi} no encontrado.")
            return None
        actual = self.primero
        while True:
            if actual.dpi == dpi:
                actual.nombres = nuevos_datos.get('nombres', actual.nombres)
                actual.apellidos = nuevos_datos.get('apellidos', actual.apellidos)
                actual.genero = nuevos_datos.get('genero', actual.genero)
                actual.telefono = nuevos_datos.get('telefono', actual.telefono)
                actual.direccion = nuevos_datos.get('direccion', actual.direccion)
                print(f"Cliente {actual.nombres} modificado.")
                print(f"DPI: {actual.dpi}\n | Nombres: {actual.nombres}\n  | Apellidos: {actual.apellidos}\n   | Género: {actual.genero}\n    | Teléfono: {actual.telefono}\n     | Dirección: {actual.direccion}\n")
                return actual
            actual = actual.siguiente
            if actual == self.primero:
                break
        return None

    def eliminar(self, dpi):
        if not self.existe_dpi(dpi):
            print(f"Cliente con DPI {dpi} no encontrado.")
            return
        actual = self.primero
        if actual is None:
            print("La lista está vacía.")
            return
        while True:
            if actual.dpi == dpi:
                if actual == self.primero and actual == self.ultimo:
                    self.primero = self.ultimo = None
                elif actual == self.primero:
                    self.primero = actual.siguiente
                    self.primero.anterior = self.ultimo
                    self.ultimo.siguiente = self.primero
                elif actual == self.ultimo:
                    self.ultimo = actual.anterior
                    self.ultimo.siguiente = self.primero
                    self.primero.anterior = self.ultimo
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                print(f"Cliente {actual.nombres} eliminado.")
                print(f"DPI: {actual.dpi}\n | Nombres: {actual.nombres}\n  | Apellidos: {actual.apellidos}\n   | Género: {actual.genero}\n    | Teléfono: {actual.telefono}\n     | Dirección: {actual.direccion}\n")
                return
            actual = actual.siguiente
            if actual == self.primero:
                break

    def mostrar_informacion(self, dpi):
        actual = self.primero
        if actual is None:
            print("La lista está vacía.")
            return None
        while True:
            if actual.dpi == dpi:
                print(f"DPI: {actual.dpi}\n | Nombres: {actual.nombres}\n  | Apellidos: {actual.apellidos}\n   | Género: {actual.genero}\n    | Teléfono: {actual.telefono}\n     | Dirección: {actual.direccion}\n")
                return actual
            actual = actual.siguiente
            if actual == self.primero:
                break
        print(f"Cliente con DPI {dpi} no encontrado.")
        return None
                    
    def mostrar(self):
        if self.primero is None:
            print("La lista está vacía.")
            return []
        clientes = []
        actual = self.primero
        while True:
            print(f"DPI: {actual.dpi}\n | Nombres: {actual.nombres}\n  | Apellidos: {actual.apellidos}\n   | Género: {actual.genero}\n    | Teléfono: {actual.telefono}\n     | Dirección: {actual.direccion}\n")
            clientes.append(actual)
            actual = actual.siguiente
            if actual == self.primero:
                break
        return clientes
            
    def carga_masiva(self, contenido:str):
        print(contenido)
        try:
            for line in contenido.split(';'):
                if line.strip():
                    datos = line.strip().split(',')
                    if len(datos) == 6:
                        dpi, nombres, apellidos, genero, telefono, direccion = map(str.strip, datos)
                        cliente = Cliente(dpi, nombres, apellidos, genero, telefono, direccion)
                        self.agregar(cliente)
            print("Carga masiva completada.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
        