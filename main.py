import tkinter as tk
from tkinter import ttk, filedialog

from src.ListaCircularDoble.ListaCircularDoble import ListaCircularDoble
from src.ArbolB.ArbolB import ArbolB
from src.Grafo.ListaAdyacencia import ListaAdyacencia

from src.Clases.Clientes import Cliente
from src.Clases.Vehiculos import Vehiculo
from src.Clases.Vertices import Vertice


lista_clientes = ListaCircularDoble()
arbol_vehiculos = ArbolB()
lista_adyacencia = ListaAdyacencia()

def cargar_datos_prueba():
    lista_clientes.agregar(Cliente("1234567890101", "Juan", "Pérez", "M", "12345678", "Ciudad de Guatemala"))
    arbol_vehiculos.insertar(Vehiculo("P001", "Toyota", "Corolla", 0.5))
    lista_adyacencia.insertar("A", "B")
    lista_adyacencia.insertar("A", "C")
    lista_adyacencia.insertar("C", "A")
    lista_adyacencia.mostrar_grafo()
    lista_adyacencia.graficar("grafo")
    print(lista_adyacencia.eliminar_grafo())
    lista_adyacencia.mostrar_grafo()

def abrir_archivo():
    print("Abriendo el cuadro de diálogo para seleccionar un archivo...")
    ruta = filedialog.askopenfilename(filetypes=[("Archivo TXT", "*.txt")])
    if ruta:
        print(f"Archivo seleccionado: {ruta}")
        try:
            with open(ruta, 'r', encoding='utf-8') as file:
                txt = file.read()
                print("Contenido del archivo:")
                print()
                print("--------------------------------------------------")
                print(txt)
                print("--------------------------------------------------")
                print()
            
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            
        return txt, ruta

def menu():
    while True:
        print("Menú de Gestión")
        print("1. Clientes")
        print("2. Vehiculos")
        print("3. Rutas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        print()

        if opcion == "1":
            gestionClientes()
        elif opcion == "2":
            gestionVehiculos()
        elif opcion == "3":
            cargar_datos_prueba()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def gestionVehiculos():
    print("Gestión de Vehiculos")
    print("1. Agregar Vehiculo")
    print("2. Modificar Vehiculo")
    print("3. Eliminar Vehiculo")
    print("4. Imprimir un Unico Vehiculo")
    print("5. Imprimir Vehiculos")
    print("6. Carga Masiva .txt")
    opcion = input("Seleccione una opción: ")
    print()
    
    if opcion == "1":
        placa = input("Ingrese Placa: ")
        
        if arbol_vehiculos.buscar(placa):
            print("El número de Placa ya existe.")
            return
        
        marca = input("Ingrese Marca: ")
        modelo = input("Ingrese Modelo: ")
        precio_por_segundo = float(input("Ingrese Precio por Segundo: "))
        
        vehiculo = Vehiculo(placa, marca, modelo, precio_por_segundo)
        print()
        arbol_vehiculos.insertar(vehiculo)
        print(f"Vehículo {marca} {modelo} agregado.")
          
    elif opcion == "2":
        placa = input("Ingrese Placa del vehículo a modificar: ")
        
        if arbol_vehiculos.buscar(placa):
            nuevos_datos = {}
            nuevos_datos['marca'] = input("Ingrese nueva Marca (deje en blanco para no modificar): ")
            nuevos_datos['modelo'] = input("Ingrese nuevo Modelo (deje en blanco para no modificar): ")
            nuevos_datos['precio_por_segundo'] = input("Ingrese nuevo Precio por Segundo (deje en blanco para no modificar): ")
            vehiculo_modificado = arbol_vehiculos.modificar(placa, {k: v for k, v in nuevos_datos.items() if v})
            if vehiculo_modificado:
                print(f"Vehículo modificado.")
                print()
        else:
            print(f"Vehículo con Placa {placa} no encontrado.")
         
    elif opcion == "3":
        placa = input("Ingrese Placa del vehículo a eliminar: ")
        vehiculo_eliminado = arbol_vehiculos.eliminar(placa)
        if vehiculo_eliminado:
            print(f"Vehículo eliminado.")
            
    elif opcion == "4":
        placa = input("Ingrese Placa del vehículo a mostrar: ")
        vehiculo = arbol_vehiculos.mostrar_informacion(placa)
        print()
        if vehiculo:
            print(f"Vehiculo encontrado.")
            
    elif opcion == "5":
        lista_vehiculos = arbol_vehiculos.obtener_todos_vehiculos()
        for vehiculo in lista_vehiculos:
            print(f"Placa: {vehiculo.placa}\n | Marca: {vehiculo.marca}\n  | Modelo: {vehiculo.modelo}\n   | Precio por segundo: {vehiculo.precio_por_segundo}\n")
       
    if opcion == "6":
        contenido, ruta = abrir_archivo()
        if contenido:
            arbol_vehiculos.cargar_masiva(contenido)
        else:
            print("No se seleccionó ningún archivo.")
    else:
        print("Opción no válida. Intente de nuevo.")

def gestionClientes():
    print("Gestión de Cliente")
    print("1. Agregar Cliente")
    print("2. Modificar Cliente")
    print("3. Eliminar Cliente")
    print("4. Imprimir un Unico Cliente")
    print("5. Imprimir Clientes")
    print("6. Carga Masiva .txt")
    opcion = input("Seleccione una opción: ")
    print()
    
    if opcion == "1":
        dpi = input("Ingrese DPI: ")
        
        if (lista_clientes.existe_dpi(dpi)):
            print("El número de DPI ya existe.")
            return
        
        nombres = input("Ingrese Nombres: ")
        apellidos = input("Ingrese Apellidos: ")
        genero = input("Ingrese Género: ")
        telefono = input("Ingrese Teléfono: ")
        direccion = input("Ingrese Dirección: ")
        cliente = Cliente(dpi, nombres, apellidos, genero, telefono, direccion)
        print()
        lista_clientes.agregar(cliente)
        print(f"Cliente {nombres} agregado.")
        
    elif opcion == "2":
        dpi = input("Ingrese DPI del cliente a modificar: ")
        
        if lista_clientes.existe_dpi(dpi):
            nuevos_datos = {}
            nuevos_datos['nombres'] = input("Ingrese nuevos Nombres (deje en blanco para no modificar): ")
            nuevos_datos['apellidos'] = input("Ingrese nuevos Apellidos (deje en blanco para no modificar): ")
            nuevos_datos['genero'] = input("Ingrese nuevo Género (deje en blanco para no modificar): ")
            nuevos_datos['telefono'] = input("Ingrese nuevo Teléfono (deje en blanco para no modificar): ")
            nuevos_datos['direccion'] = input("Ingrese nueva Dirección (deje en blanco para no modificar): ")
            lista_clientes.modificar(dpi, {k: v for k, v in nuevos_datos.items() if v})
        else:
            print(f"Cliente con DPI {dpi} no encontrado.")
            
    elif opcion == "3":
        dpi = input("Ingrese DPI del cliente a eliminar: ")
        lista_clientes.eliminar(dpi)
    elif opcion == "4":
        dpi = input("Ingrese DPI del cliente a mostrar: ")
        lista_clientes.mostrar_informacion(dpi)
    elif opcion == "5":
        lista_clientes.mostrar()
    elif opcion == "6":
        contenido, ruta = abrir_archivo()
        if contenido:
            lista_clientes.carga_masiva(contenido)
        else:
            print("No se seleccionó ningún archivo.")
    else:
        print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    cargar_datos_prueba()
    menu()