from src.ArbolB.NodoArbolB import NodoArbolB
from src.Clases.Vehiculos import Vehiculo

class ArbolB:    
    def __init__(self, orden=5):
        self.ORDEN = orden
        self.raiz = NodoArbolB(self.ORDEN)

    def insertar(self, vehiculo: Vehiculo):
        raiz = self.raiz
        if raiz.n == 2 * self.ORDEN - 1:
            nuevo_nodo = NodoArbolB(self.ORDEN)
            self.raiz = nuevo_nodo
            nuevo_nodo.hoja = False
            nuevo_nodo.hijos[0] = raiz
            self.dividir_hijo(nuevo_nodo, 0, raiz)
            self.insertar_no_lleno(nuevo_nodo, vehiculo)
        else:
            self.insertar_no_lleno(raiz, vehiculo)

    def dividir_hijo(self, nodo_padre, indice, nodo_lleno):
        nuevo_nodo = NodoArbolB(self.ORDEN)
        nuevo_nodo.hoja = nodo_lleno.hoja
        nuevo_nodo.n = self.ORDEN - 1
        for k in range(self.ORDEN - 1):
            nuevo_nodo.llaves[k] = nodo_lleno.llaves[k + self.ORDEN]
        if not nodo_lleno.hoja:
            for k in range(self.ORDEN):
                nuevo_nodo.hijos[k] = nodo_lleno.hijos[k + self.ORDEN]
        nodo_lleno.n = self.ORDEN - 1
        for k in range(nodo_padre.n, indice, -1):
            nodo_padre.hijos[k + 1] = nodo_padre.hijos[k]
        nodo_padre.hijos[indice + 1] = nuevo_nodo
        for k in range(nodo_padre.n - 1, indice - 1, -1):
            nodo_padre.llaves[k + 1] = nodo_padre.llaves[k]
        nodo_padre.llaves[indice] = nodo_lleno.llaves[self.ORDEN - 1]
        nodo_padre.n += 1

    def insertar_no_lleno(self, nodo, vehiculo: Vehiculo):
        indice = nodo.n - 1
        if nodo.hoja:
            while indice >= 0 and vehiculo.placa < nodo.llaves[indice].placa:
                nodo.llaves[indice + 1] = nodo.llaves[indice]
                indice -= 1
            nodo.llaves[indice + 1] = vehiculo
            nodo.n += 1
        else:
            while indice >= 0 and vehiculo.placa < nodo.llaves[indice].placa:
                indice -= 1
            indice += 1
            if nodo.hijos[indice].n == 2 * self.ORDEN - 1:
                self.dividir_hijo(nodo, indice, nodo.hijos[indice])
                if vehiculo.placa > nodo.llaves[indice].placa:
                    indice += 1
            self.insertar_no_lleno(nodo.hijos[indice], vehiculo)

    def cargar_masiva(self, contenido):
        try:
            for line in contenido.split(';'):
                if line.strip():
                    datos = line.strip().split(':')
                    if len(datos) == 4:
                        placa = datos[0].strip()
                        marca = datos[1].strip()
                        modelo = datos[2].strip()
                        precio_por_segundo = float(datos[3].strip())
                        vehiculo = Vehiculo(placa, marca, modelo, precio_por_segundo)
                        self.insertar(vehiculo)
            print("Carga masiva de vehículos completada.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def buscar(self, placa, nodo=None):
        if placa is None:
            return None
        if nodo is None:
            nodo = self.raiz
        indice = 0
        while indice < nodo.n and placa > nodo.llaves[indice].placa:
            indice += 1
        if indice < nodo.n and placa == nodo.llaves[indice].placa:
            return nodo.llaves[indice]
        elif nodo.hoja:
            return None
        else:
            return self.buscar(placa, nodo.hijos[indice])

    def modificar(self, placa, nuevos_datos):
        if placa is None:
            print("Placa no puede ser None.")
            return None
        vehiculo = self.buscar(placa)
        if vehiculo:
            vehiculo.marca = nuevos_datos.get('marca', vehiculo.marca)
            vehiculo.modelo = nuevos_datos.get('modelo', vehiculo.modelo)
            vehiculo.precio_por_segundo = nuevos_datos.get('precio_por_segundo', vehiculo.precio_por_segundo)
            print(f"Vehículo con placa {placa} modificado.")
            print(f"Placa: {vehiculo.placa}\n | Marca: {vehiculo.marca}\n  | Modelo: {vehiculo.modelo}\n   | Precio por segundo: {vehiculo.precio_por_segundo}")
            return vehiculo
        else:
            print(f"Vehículo con placa {placa} no encontrado.")
            return None

    def eliminar(self, placa):
        if placa is None:
            print("Placa no puede ser None.")
            return None
        vehiculo = self.buscar(placa)
        if vehiculo:
            self.eliminar_aux(self.raiz, placa)
            if self.raiz.n == 0:
                if not self.raiz.hoja:
                    self.raiz = self.raiz.hijos[0]
                else:
                    self.raiz = NodoArbolB(self.ORDEN)
            print(f"Vehículo eliminado:")
            print(f"Placa: {vehiculo.placa}\n | Marca: {vehiculo.marca}\n  | Modelo: {vehiculo.modelo}\n   | Precio por segundo: {vehiculo.precio_por_segundo}")
            return vehiculo
        else:
            print(f"Vehículo con placa {placa} no encontrado.")
            return None
    
    def obtener_todos_vehiculos(self, nodo=None, lista_vehiculos=None):
        if lista_vehiculos is None:
            lista_vehiculos = []
        if nodo is None:
            nodo = self.raiz
        for i in range(nodo.n):
            if not nodo.hoja:
                self.obtener_todos_vehiculos(nodo.hijos[i], lista_vehiculos)
            lista_vehiculos.append(nodo.llaves[i])
        if not nodo.hoja:
            self.obtener_todos_vehiculos(nodo.hijos[nodo.n], lista_vehiculos)
        return lista_vehiculos
         
    def eliminar_aux(self, nodo, placa):
        indice = 0
        while indice < nodo.n and placa > nodo.llaves[indice].placa:
            indice += 1
        if indice < nodo.n and placa == nodo.llaves[indice].placa:
            if nodo.hoja:
                for j in range(indice, nodo.n - 1):
                    nodo.llaves[j] = nodo.llaves[j + 1]
                nodo.n -= 1
            else:
                if nodo.hijos[indice].n >= self.ORDEN:
                    predecesor = self.obtener_predecesor(nodo, indice)
                    nodo.llaves[indice] = predecesor
                    self.eliminar_aux(nodo.hijos[indice], predecesor.placa)
                elif nodo.hijos[indice + 1].n >= self.ORDEN:
                    sucesor = self.obtener_sucesor(nodo, indice)
                    nodo.llaves[indice] = sucesor
                    self.eliminar_aux(nodo.hijos[indice + 1], sucesor.placa)
                else:
                    self.unir(nodo, indice)
                    self.eliminar_aux(nodo.hijos[indice], placa)
        else:
            if nodo.hoja:
                return
            flag = (indice == nodo.n)
            if nodo.hijos[indice].n < self.ORDEN:
                self.llenar(nodo, indice)
            if flag and indice > nodo.n:
                self.eliminar_aux(nodo.hijos[indice - 1], placa)
            else:
                self.eliminar_aux(nodo.hijos[indice], placa)

    def obtener_predecesor(self, nodo, indice):
        actual = nodo.hijos[indice]
        while not actual.hoja:
            actual = actual.hijos[actual.n]
        return actual.llaves[actual.n - 1]

    def obtener_sucesor(self, nodo, indice):
        actual = nodo.hijos[indice + 1]
        while not actual.hoja:
            actual = actual.hijos[0]
        return actual.llaves[0]

    def unir(self, nodo, indice):
        hijo = nodo.hijos[indice]
        hermano = nodo.hijos[indice + 1]
        hijo.llaves[self.ORDEN - 1] = nodo.llaves[indice]
        for j in range(hermano.n):
            hijo.llaves[j + self.ORDEN] = hermano.llaves[j]
        if not hijo.hoja:
            for j in range(hermano.n + 1):
                hijo.hijos[j + self.ORDEN] = hermano.hijos[j]
        for j in range(indice + 1, nodo.n):
            nodo.llaves[j - 1] = nodo.llaves[j]
        for j in range(indice + 2, nodo.n + 1):
            nodo.hijos[j - 1] = nodo.hijos[j]
        hijo.n += hermano.n + 1
        nodo.n -= 1
        
    def llenar(self, nodo, indice):
        if indice != 0 and nodo.hijos[indice - 1].n >= self.ORDEN:
            self.prestar_anterior(nodo, indice)
        elif indice != nodo.n and nodo.hijos[indice + 1].n >= self.ORDEN:
            self.prestar_siguiente(nodo, indice)
        else:
            if indice != nodo.n:
                self.unir(nodo, indice)
            else:
                self.unir(nodo, indice - 1)

    def prestar_anterior(self, nodo, indice):
        hijo = nodo.hijos[indice]
        hermano = nodo.hijos[indice - 1]
        for j in range(hijo.n - 1, -1, -1):
            hijo.llaves[j + 1] = hijo.llaves[j]
        if not hijo.hoja:
            for j in range(hijo.n, -1, -1):
                hijo.hijos[j + 1] = hijo.hijos[j]
        hijo.llaves[0] = nodo.llaves[indice - 1]
        if not hijo.hoja:
            hijo.hijos[0] = hermano.hijos[hermano.n]
        nodo.llaves[indice - 1] = hermano.llaves[hermano.n - 1]
        hijo.n += 1
        hermano.n -= 1

    def prestar_siguiente(self, nodo, indice):
        hijo = nodo.hijos[indice]
        hermano = nodo.hijos[indice + 1]
        hijo.llaves[hijo.n] = nodo.llaves[indice]
        if not hijo.hoja:
            hijo.hijos[hijo.n + 1] = hermano.hijos[0]
        nodo.llaves[indice] = hermano.llaves[0]
        for j in range(1, hermano.n):
            hermano.llaves[j - 1] = hermano.llaves[j]
        if not hermano.hoja:
            for j in range(1, hermano.n + 1):
                hermano.hijos[j - 1] = hermano.hijos[j]
        hijo.n += 1
        hermano.n -= 1

    def mostrar_informacion(self, placa):
        if placa is None:
            print("Placa no puede ser None.")
            return None
        vehiculo = self.buscar(placa)
        if vehiculo:
            print(f"Placa: {vehiculo.placa}\n | Marca: {vehiculo.marca}\n  | Modelo: {vehiculo.modelo}\n   | Precio por segundo: {vehiculo.precio_por_segundo}")
        else:
            print(f"Vehículo con placa {placa} no encontrado.")