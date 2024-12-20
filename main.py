import tkinter as tk
from tkinter import ttk, filedialog


from src.ListaCircularDoble.ListaCircularDoble import ListaCircularDoble
from src.ListaCircularDoble.Usuario import Usuario

lista_usuarios = ListaCircularDoble()

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
        print("1. Usuarios")
        print("2. Vehiculos")
        print("3. Rutas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        print()

        if opcion == "1":
            gestionUsuarios()
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def gestionUsuarios():
    print("Gestión de Usuario")
    print("1. Agregar Usuario")
    print("2. Modificar Usuario")
    print("3. Eliminar Usuario")
    print("4. Imprimir un Unico Usuario")
    print("5. Imprimir Usuarios")
    print("6. Carga Masiva .txt")
    opcion = input("Seleccione una opción: ")
    print()
    
    if opcion == "1":
        dpi = input("Ingrese DPI: ")
        nombres = input("Ingrese Nombres: ")
        apellidos = input("Ingrese Apellidos: ")
        genero = input("Ingrese Género: ")
        telefono = input("Ingrese Teléfono: ")
        direccion = input("Ingrese Dirección: ")
        usuario = Usuario(dpi, nombres, apellidos, genero, telefono, direccion)
        print()
        lista_usuarios.agregar(usuario)
        print(f"Usuario {nombres} agregado.")
    elif opcion == "2":
        dpi = input("Ingrese DPI del usuario a modificar: ")
        nuevos_datos = {}
        nuevos_datos['nombres'] = input("Ingrese nuevos Nombres (deje en blanco para no modificar): ")
        nuevos_datos['apellidos'] = input("Ingrese nuevos Apellidos (deje en blanco para no modificar): ")
        nuevos_datos['genero'] = input("Ingrese nuevo Género (deje en blanco para no modificar): ")
        nuevos_datos['telefono'] = input("Ingrese nuevo Teléfono (deje en blanco para no modificar): ")
        nuevos_datos['direccion'] = input("Ingrese nueva Dirección (deje en blanco para no modificar): ")
        lista_usuarios.modificar(dpi, {k: v for k, v in nuevos_datos.items() if v})
    elif opcion == "3":
        dpi = input("Ingrese DPI del usuario a eliminar: ")
        lista_usuarios.eliminar(dpi)
    elif opcion == "4":
        dpi = input("Ingrese DPI del usuario a mostrar: ")
        lista_usuarios.mostrar_informacion(dpi)
    elif opcion == "5":
        lista_usuarios.mostrar()
    elif opcion == "6":
        contenido, ruta = abrir_archivo()
        if contenido:
            lista_usuarios.carga_masiva(contenido)
        else:
            print("No se seleccionó ningún archivo.")
    elif opcion == "7":
        pass
    else:
        print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()