import tkinter as tk
import os
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

from src.ListaCircularDoble.ListaCircularDoble import ListaCircularDoble
from src.ArbolB.ArbolB import ArbolB
from src.Grafo.ListaAdyacencia import ListaAdyacencia

from src.Clases.Clientes import Cliente
from src.Clases.Vehiculos import Vehiculo


lista_clientes = ListaCircularDoble()
arbol_vehiculos = ArbolB()
lista_adyacencia = ListaAdyacencia()

ruta_grafo = ""

def cargar_datos_prueba():
    lista_clientes.agregar(Cliente("1234567890101", "Juan", "Pérez", "M", "12345678", "Ciudad de Guatemala"))
    arbol_vehiculos.insertar(Vehiculo("P001", "Toyota", "Corolla", 0.5))
    
    lista_adyacencia.insertar("A", "B", 140)
    lista_adyacencia.insertar("A", "C", 250)
    lista_adyacencia.insertar("C", "A", 200)
    lista_adyacencia.mostrar_grafo()
    lista_adyacencia.graficar("grafo")
    print(lista_adyacencia.eliminar_grafo())
    lista_adyacencia.mostrar_grafo()

#########################################################################################################################
# Funciones para interfaz grafo

def cargar_rutas():
    print("Abriendo el cuadro de diálogo para seleccionar un archivo...")
    ruta = filedialog.askopenfilename()
    if ruta:
        print(f"Archivo seleccionado: {ruta}")
        with open(ruta, 'r', encoding='utf-8') as file:
            contenido = file.read()
            print("Contenido del archivo:")
            print()
            print("--------------------------------------------------")
            print(contenido)
            print("--------------------------------------------------")
            print()
    
    lista_adyacencia.cargar_rutas_desde_contenido(contenido)
    messagebox.showinfo("Éxito", "Rutas cargadas exitosamente.")            

def eliminar_grafo():
    print("Eliminando el grafo...")
    confirmacion = messagebox.askyesno("Eliminar Grafo", "¿Seguro que desea eliminar el grafo?")
    if confirmacion:
        print(lista_adyacencia.eliminar_grafo())
        generar_grafo()
    else:
        print("Operación cancelada.")

def generar_grafo():
    print("Generando el grafo...")
    global ruta_grafo
    ruta_grafo = lista_adyacencia.graficar("grafo")
    mostrar_imagen()

def mostrar_imagen(event=None):
    image_path = ruta_grafo
    if image_path and os.path.exists(image_path):
        img = Image.open(image_path)
        window_width = tab_grafo.winfo_width()
        window_height = tab_grafo.winfo_height() - 100
        aspect_ratio = img.width / img.height
        if img.width > img.height:
            new_width = window_width
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = window_height
            new_width = int(new_height * aspect_ratio)
        if new_width > 0 and new_height > 0:
            img = img.resize((new_width, new_height))
            img = ImageTk.PhotoImage(img)
            panel.config(image=img)
            panel.image = img

#########################################################################################################################
# Funciones para interfaz clientes

def agregar_cliente():
    dpi = entry_dpi.get()
    nombres = entry_nombres.get()
    apellidos = entry_apellidos.get()
    genero = entry_genero.get()
    telefono = entry_telefono.get()
    direccion = entry_direccion.get()
    
    if lista_clientes.existe_dpi(dpi):
        messagebox.showerror("Error", "El número de DPI ya existe.")
        return
    
    cliente = Cliente(dpi, nombres, apellidos, genero, telefono, direccion)
    lista_clientes.agregar(cliente)
    messagebox.showinfo("Éxito", f"Cliente {nombres} agregado.")
    limpiar_campos()

def limpiar_campos():
    entry_dpi.delete(0, tk.END)
    entry_nombres.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)

def modificar_cliente():
    dpi = entry_dpi.get()
    if not lista_clientes.existe_dpi(dpi):
        messagebox.showerror("Error", "El cliente no existe.")
        return
    
    nuevos_datos = {
        'nombres': entry_nombres.get(),
        'apellidos': entry_apellidos.get(),
        'genero': entry_genero.get(),
        'telefono': entry_telefono.get(),
        'direccion': entry_direccion.get()
    }
    lista_clientes.modificar(dpi, {k: v for k, v in nuevos_datos.items() if v})
    messagebox.showinfo("Éxito", f"Cliente {dpi} modificado.")
    limpiar_campos()

def eliminar_cliente():
    dpi = entry_dpi.get()
    if not lista_clientes.existe_dpi(dpi):
        messagebox.showerror("Error", "El cliente no existe.")
        return
    
    lista_clientes.eliminar(dpi)
    messagebox.showinfo("Éxito", f"Cliente {dpi} eliminado.")
    limpiar_campos()

def cargar_clientes():
    print("Abriendo el cuadro de diálogo para seleccionar un archivo...")
    ruta = filedialog.askopenfilename()
    if ruta:
        print(f"Archivo seleccionado: {ruta}")
        with open(ruta, 'r', encoding='utf-8') as file:
            contenido = file.read()
            print("Contenido del archivo:")
            print()
            print("--------------------------------------------------")
            print(contenido)
            print("--------------------------------------------------")
            print()
    
    lista_clientes.carga_masiva(contenido)
    messagebox.showinfo("Éxito", "Clientes cargados exitosamente.") 

#########################################################################################################################

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
            gestionRutas()
            
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def gestionRutas():
    print("Gestión de Rutas")
    print("1. Agregar Ruta")
    print("2. Modificar Ruta")
    print("3. Eliminar Grafo de Rutas")
    print("4. Imprimir Rutas")
    print("5. Carga Masiva .txt")
    opcion = input("Seleccione una opción: ")
    print()
    
    if opcion == "1":
        origen = input("Ingrese Origen: ")
        destino = input("Ingrese Destino: ")
        tiempo = int(input("Ingrese Tiempo: "))
        lista_adyacencia.insertar(origen, destino, tiempo)
        print()
        
    elif opcion == "2":
        pass
            
    elif opcion == "3":
        print("Seguro de eliminar el Grafo? (S/N)")
        confirmacion = input("Seleccione una opción: ")
        if confirmacion.lower() == "s":
            lista_adyacencia.eliminar_grafo()
            print("Grafo eliminado.")
        else:
            print("Operación cancelada.")
        
    elif opcion == "4":
        lista_adyacencia.mostrar_grafo()
        
    elif opcion == "5":
        lista_adyacencia.eliminar_grafo()
        contenido, ruta = abrir_archivo()
        if contenido:
            lista_adyacencia.cargar_rutas_desde_contenido(contenido)
        else:
            print("No se seleccionó ningún archivo.")
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

"""if __name__ == "__main__":
    cargar_datos_prueba()
    menu()"""

#########################################################################################################################

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Grafos")

# Obtener el tamaño de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Definir el tamaño de la ventana
window_width = 700
window_height = 750

# Calcular la posición x e y para centrar la ventana
position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)

# Establecer la geometría de la ventana
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

#########################################################################################################################

# Crear el Notebook
tab_control = ttk.Notebook(root)

# Crear los frames para cada pestaña
tab_grafo = ttk.Frame(tab_control, style='TFrame')
tab_clientes = ttk.Frame(tab_control, style='TFrame')
tab_vehiculos = ttk.Frame(tab_control, style='TFrame')
tab_viajes = ttk.Frame(tab_control, style='TFrame')

# Añadir los frames al Notebook
tab_control.add(tab_grafo, text='Gestión de Rutas')
tab_control.add(tab_clientes, text='Menú de Clientes')
tab_control.add(tab_vehiculos, text='Menú de Vehículos')
tab_control.add(tab_viajes, text='Menú de Viajes')

# Empaquetar el Notebook en la ventana principal
tab_control.pack(expand=1, fill='both')

#########################################################################################################################

# Crear un frame contenedor para los botones en la parte superior de la pestaña del grafo
frame_botones_container_grafo = tk.Frame(tab_grafo, bg="white")
frame_botones_container_grafo.pack(side=tk.TOP, fill=tk.X, pady=10)

frame_botones = tk.Frame(frame_botones_container_grafo, bg="white")
frame_botones.pack(expand=True)

# Añadir contenido a la pestaña de grafo
btn_cargar_rutas = tk.Button(frame_botones, text="Cargar Rutas", command=cargar_rutas, width=20, height=2, bg = "#FFF2C2", fg = "black")
btn_generar_grafo = tk.Button(frame_botones, text="Generar Grafo", command=generar_grafo, width=20, height=2, bg = "#FFF2C2", fg = "black")
btn_eliminar_grafo = tk.Button(frame_botones, text="Eliminar Grafo", command=eliminar_grafo, width=20, height=2, bg = "#FFF2C2", fg = "black")

btn_cargar_rutas.pack(side=tk.LEFT, padx=10)
btn_generar_grafo.pack(side=tk.LEFT, padx=10)
btn_eliminar_grafo.pack(side=tk.LEFT, padx=10)

# Añadir un frame para la imagen en la parte inferior de la pestaña 1
frame_imagen = tk.Frame(tab_grafo, bg="white")
frame_imagen.pack(expand=True, fill='both')

#########################################################################################################################

# Crear un frame contenedor para los botones en la parte superior de la pestaña de clientes
frame_botones_container_clientes = tk.Frame(tab_clientes, bg="white")
frame_botones_container_clientes.pack(side=tk.TOP, fill=tk.X, pady=10)

frame_botones_clientes = tk.Frame(frame_botones_container_clientes, bg="white")
frame_botones_clientes.pack(expand=True)

# Añadir botones para las acciones de clientes
btn_carga_masiva = tk.Button(frame_botones_clientes, text="Carga Masiva", command=cargar_clientes, bg="#FFF2C2", fg="black")
btn_carga_masiva.pack(side=tk.LEFT, padx=5)

btn_agregar_cliente = tk.Button(frame_botones_clientes, text="Agregar Cliente", command=agregar_cliente, bg="#FFF2C2", fg="black")
btn_agregar_cliente.pack(side=tk.LEFT, padx=5)

btn_modificar_cliente = tk.Button(frame_botones_clientes, text="Modificar Cliente", command=modificar_cliente, bg="#FFF2C2", fg="black")
btn_modificar_cliente.pack(side=tk.LEFT, padx=5)

btn_eliminar_cliente = tk.Button(frame_botones_clientes, text="Eliminar Cliente", command=eliminar_cliente, bg="#FFF2C2", fg="black")
btn_eliminar_cliente.pack(side=tk.LEFT, padx=5)

btn_limpiar_campos = tk.Button(frame_botones_clientes, text="Limpiar Campos", command=limpiar_campos, bg="#FFF2C2", fg="black")
btn_limpiar_campos.pack(side=tk.LEFT, padx=5)

# Crear un frame contenedor para los campos de entrada en la pestaña de clientes
frame_campos_clientes = tk.Frame(tab_clientes, bg="white")
frame_campos_clientes.pack(side=tk.RIGHT, expand=True, fill='both', padx=20, pady=20)

# Añadir campos de entrada para los datos del cliente
tk.Label(frame_campos_clientes, text="DPI:", bg="white").grid(row=0, column=0, sticky=tk.W, pady=5)
entry_dpi = tk.Entry(frame_campos_clientes)
entry_dpi.grid(row=0, column=1, pady=5)

tk.Label(frame_campos_clientes, text="Nombres:", bg="white").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_nombres = tk.Entry(frame_campos_clientes)
entry_nombres.grid(row=1, column=1, pady=5)

tk.Label(frame_campos_clientes, text="Apellidos:", bg="white").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_apellidos = tk.Entry(frame_campos_clientes)
entry_apellidos.grid(row=2, column=1, pady=5)

tk.Label(frame_campos_clientes, text="Género:", bg="white").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_genero = tk.Entry(frame_campos_clientes)
entry_genero.grid(row=3, column=1, pady=5)

tk.Label(frame_campos_clientes, text="Teléfono:", bg="white").grid(row=4, column=0, sticky=tk.W, pady=5)
entry_telefono = tk.Entry(frame_campos_clientes)
entry_telefono.grid(row=4, column=1, pady=5)

tk.Label(frame_campos_clientes, text="Dirección:", bg="white").grid(row=5, column=0, sticky=tk.W, pady=5)
entry_direccion = tk.Entry(frame_campos_clientes)
entry_direccion.grid(row=5, column=1, pady=5)

#########################################################################################################################

# Establecer el estilo para el fondo blanco de las pestañas
style = ttk.Style()
style.configure('TFrame', background='white')

# Vincular el evento de cambio de tamaño de la ventana a la función mostrar_imagen
tab_grafo.bind("<Configure>", mostrar_imagen)

# Iniciar el bucle principal de la aplicación
root.mainloop()