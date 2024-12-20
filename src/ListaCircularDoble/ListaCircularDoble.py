from src.ListaCircularDoble.Usuario import Usuario

class ListaCircularDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar(self, usuario):
        if self.primero is None:
            self.primero = self.ultimo = usuario
            self.primero.siguiente = self.primero.anterior = self.primero
        else:
            actual = self.primero
            while actual.siguiente != self.primero and int(actual.dpi) < int(usuario.dpi):
                actual = actual.siguiente
            if actual == self.primero and int(usuario.dpi) < int(actual.dpi):
                usuario.siguiente = self.primero
                usuario.anterior = self.ultimo
                self.primero.anterior = usuario
                self.ultimo.siguiente = usuario
                self.primero = usuario
            elif actual == self.ultimo and int(usuario.dpi) > int(actual.dpi):
                usuario.siguiente = self.primero
                usuario.anterior = self.ultimo
                self.ultimo.siguiente = usuario
                self.primero.anterior = usuario
                self.ultimo = usuario
            else:
                usuario.siguiente = actual
                usuario.anterior = actual.anterior
                actual.anterior.siguiente = usuario
                actual.anterior = usuario
                    
    def modificar(self, dpi, nuevos_datos):
        actual = self.primero
        if actual is None:
            print("La lista está vacía.")
            return
        while True:
            if actual.dpi == dpi:
                actual.nombres = nuevos_datos.get('nombres', actual.nombres)
                actual.apellidos = nuevos_datos.get('apellidos', actual.apellidos)
                actual.genero = nuevos_datos.get('genero', actual.genero)
                actual.telefono = nuevos_datos.get('telefono', actual.telefono)
                actual.direccion = nuevos_datos.get('direccion', actual.direccion)
                print(f"Usuario {actual.nombres} modificado.")
                print(f"DPI: {actual.dpi}\n | Nombres: {actual.nombres}\n  | Apellidos: {actual.apellidos}\n   | Género: {actual.genero}\n    | Teléfono: {actual.telefono}\n     | Dirección: {actual.direccion}\n")
                return
            actual = actual.siguiente
            if actual == self.primero:
                break
        print(f"Usuario con DPI {dpi} no encontrado.")

    def eliminar(self, dpi):
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
                print(f"Usuario {actual.nombres} eliminado.")
                print(f"DPI: {actual.dpi}\n | Nombres: {actual.nombres}\n  | Apellidos: {actual.apellidos}\n   | Género: {actual.genero}\n    | Teléfono: {actual.telefono}\n     | Dirección: {actual.direccion}\n")
                return
            actual = actual.siguiente
            if actual == self.primero:
                break
        print(f"Usuario con DPI {dpi} no encontrado.")

    def mostrar_informacion(self, dpi):
        actual = self.primero
        if actual is None:
            print("La lista está vacía.")
            return
        while True:
            if actual.dpi == dpi:
                print(f"DPI: {actual.dpi}\n | Nombres: {actual.nombres}\n  | Apellidos: {actual.apellidos}\n   | Género: {actual.genero}\n    | Teléfono: {actual.telefono}\n     | Dirección: {actual.direccion}\n")
                return
            actual = actual.siguiente
            if actual == self.primero:
                break
        print(f"Usuario con DPI {dpi} no encontrado.")
                    
    def mostrar(self):
        if self.primero is None:
            print("La lista está vacía.")
            return
        actual = self.primero
        while True:
            print(f"DPI: {actual.dpi}\n | Nombres: {actual.nombres}\n  | Apellidos: {actual.apellidos}\n   | Género: {actual.genero}\n    | Teléfono: {actual.telefono}\n     | Dirección: {actual.direccion}\n")
            actual = actual.siguiente
            if actual == self.primero:
                break
            
    def carga_masiva(self, contenido:str):
        print(contenido)
        try:
            for line in contenido.split(';'):
                if line.strip():
                    datos = line.strip().split(',')
                    if len(datos) == 6:
                        dpi, nombres, apellidos, genero, telefono, direccion = map(str.strip, datos)
                        usuario = Usuario(dpi, nombres, apellidos, genero, telefono, direccion)
                        self.agregar(usuario)
            print("Carga masiva completada.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")