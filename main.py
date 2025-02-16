import tkinter as tk
import os, datetime, random
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

from src.Estructuras.ListaCircularDoble.ListaCircularDoble import ListaCircularDoble
from src.Estructuras.ArbolB.ArbolB import ArbolB
from src.Estructuras.Grafo.ListaAdyacencia import ListaAdyacencia

from src.Clases.Clientes import Cliente
from src.Clases.Vehiculos import Vehiculo
from src.Clases.Viajes import Viaje

lista_clientes = ListaCircularDoble()
arbol_vehiculos = ArbolB()
lista_adyacencia = ListaAdyacencia()

ruta_grafo = ""

def cargar_datos_prueba():
    lista_clientes.agregar(Cliente("1234567890101", "Juan", "Pérez", "Masculino", "12345678", "Ciudad de Guatemala"))
    arbol_vehiculos.insertar(Vehiculo("P001", "Toyota", "Corolla", 9000))
    
    """lista_adyacencia.insertar("A", "B", 140)
    lista_adyacencia.insertar("A", "C", 250)
    lista_adyacencia.insertar("C", "A", 200)
    lista_adyacencia.mostrar_grafo()
    lista_adyacencia.graficar("grafo")
    print(lista_adyacencia.eliminar_grafo())
    lista_adyacencia.mostrar_grafo()"""

def limpiar_campos():
    entry_dpi.config(state='normal')
    entry_dpi.delete(0, tk.END)
    entry_nombres.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)
    
    entry_placa.config(state='normal')
    entry_placa.delete(0, tk.END)
    entry_marca.delete(0, tk.END)
    entry_modelo.delete(0, tk.END)
    entry_precio_por_segundo.delete(0, tk.END)

def mostrar_ruta_corta():
    inicio = "Cadiz"
    final = "Madrid"
    ruta = lista_adyacencia.obtener_rutas_desde(inicio, final)
    print(ruta)
    if ruta:
        resultado = []
        actual = ruta.inicio
        while actual is not None:
            resultado.append(actual.nombre.nombre)
            actual = actual.siguiente
        print(f"Ruta más corta desde {inicio} hasta {final}: {resultado}")
    else:
        print(f"No se encontró una ruta desde {inicio} hasta {final}")

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
    llenar_tablas_viajes()

def eliminar_grafo():
    print("Eliminando el grafo...")
    confirmacion = messagebox.askyesno("Eliminar Grafo", "¿Seguro que desea eliminar el grafo?")
    if confirmacion:
        print(lista_adyacencia.eliminar_grafo())
        generar_grafo()
        llenar_tablas_viajes()
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
        window_width = root.winfo_width()
        window_height = root.winfo_height() - 100
        aspect_ratio = img.width / img.height
        scale_factor = 0.9  # Factor de escala para reducir el tamaño de la imagen
        new_width = int(window_width * scale_factor)
        new_height = int(window_height * scale_factor)
        if img.width > img.height:
            new_width = min(new_width, img.width)
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = min(new_height, img.height)
            new_width = int(new_height * aspect_ratio)
        if new_width > 0 and new_height > 0:
            img = img.resize((new_width, new_height))
            img = ImageTk.PhotoImage(img)
            panel.config(image=img)
            panel.image = img

#########################################################################################################################
# Funciones para interfaz clientes

def agregar_cliente():
    dpi = entry_dpi.get().strip()
    nombres = entry_nombres.get().strip()
    apellidos = entry_apellidos.get().strip()
    genero = entry_genero.get().strip()
    telefono = entry_telefono.get().strip()
    direccion = entry_direccion.get().strip()
    
    if lista_clientes.existe_dpi(dpi):
        messagebox.showerror("Error", "El número de DPI ya existe.")
        return
    
    cliente = Cliente(dpi, nombres, apellidos, genero, telefono, direccion)
    lista_clientes.agregar(cliente)
    messagebox.showinfo("Éxito", f"Cliente {nombres} agregado.")
    limpiar_campos()
    actualizar_tabla_clientes()

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
    actualizar_tabla_clientes()

def eliminar_cliente():
    dpi = entry_dpi.get()
    if not lista_clientes.existe_dpi(dpi):
        messagebox.showerror("Error", "El cliente no existe.")
        return
    
    lista_clientes.eliminar(dpi)
    messagebox.showinfo("Éxito", f"Cliente {dpi} eliminado.")
    limpiar_campos()
    actualizar_tabla_clientes()

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
    actualizar_tabla_clientes()
    llenar_tablas_viajes()
    limpiar_campos()

def actualizar_tabla_clientes():
    for row in tabla_clientes.get_children():
        tabla_clientes.delete(row)
    for index, cliente in enumerate(lista_clientes.mostrar()):
        if index % 2 == 0:
            tabla_clientes.insert("", "end", values=(cliente.dpi, cliente.nombres, cliente.apellidos, cliente.genero, cliente.telefono, cliente.direccion), tags=('evenrow',))
        else:
            tabla_clientes.insert("", "end", values=(cliente.dpi, cliente.nombres, cliente.apellidos, cliente.genero, cliente.telefono, cliente.direccion), tags=('oddrow',))

def seleccionar_fila_clientes(event):
    selected_items = tabla_clientes.selection()
    if selected_items:
        selected_item = tabla_clientes.selection()[0]
        valores = tabla_clientes.item(selected_item, 'values')
        
        entry_dpi.config(state='normal')
        entry_dpi.delete(0, tk.END)
        entry_dpi.insert(0, valores[0])
        entry_dpi.config(state='readonly')
            
        entry_nombres.delete(0, tk.END)
        entry_nombres.insert(0, valores[1])
        entry_apellidos.delete(0, tk.END)
        entry_apellidos.insert(0, valores[2])
        entry_genero.delete(0, tk.END)
        entry_genero.insert(0, valores[3])
        entry_telefono.delete(0, tk.END)
        entry_telefono.insert(0, valores[4])
        entry_direccion.delete(0, tk.END)
        entry_direccion.insert(0, valores[5])

def imprimir_estructura_clientes():
    lista_clientes.graficar("clientes_lista_circular_doble")
    messagebox.showinfo("Éxito", "Estructura de la lista circular doble generada exitosamente.")

#########################################################################################################################
# Funciones para interfaz vehículos

def agregar_vehiculo():
    placa = entry_placa.get().strip()
    marca = entry_marca.get().strip()
    modelo = entry_modelo.get().strip()
    precio_por_segundo = float(entry_precio_por_segundo.get().strip())
    
    if arbol_vehiculos.buscar(placa):
        messagebox.showerror("Error", "El número de DPI ya existe.")
        return
    
    vehiculo = Vehiculo(placa, marca, modelo, precio_por_segundo)
    arbol_vehiculos.insertar(vehiculo)
    messagebox.showinfo("Éxito", f"Vehiculo con placas: {placa} agregado.")
    limpiar_campos()
    actualizar_tabla_vehiculos()
    
def modificar_vehiculo():
    placa = entry_placa.get()
    if not arbol_vehiculos.buscar(placa):
        messagebox.showerror("Error", "El vehiculo no existe.")
        return
    
    nuevos_datos = {
        'marca': entry_marca.get(),
        'modelo': entry_modelo.get(),
        'precio_por_segundo': entry_precio_por_segundo.get(),
    }
    arbol_vehiculos.modificar(placa, {k: v for k, v in nuevos_datos.items() if v})
    messagebox.showinfo("Éxito", f"Vehiculo con placas: {placa} modificado.")
    limpiar_campos()
    actualizar_tabla_vehiculos()

def eliminar_vehiculo():
    placa = entry_placa.get()
    if not arbol_vehiculos.buscar(placa):
        messagebox.showerror("Error", "El vehiculo no existe.")
        return
    
    arbol_vehiculos.eliminar(placa)
    messagebox.showinfo("Éxito", f"Vehiculo con placas: {placa} eliminado.")
    limpiar_campos()
    actualizar_tabla_vehiculos()

def cargar_vehiculos():
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
    
    arbol_vehiculos.cargar_masiva(contenido)
    messagebox.showinfo("Éxito", "Vehiculos cargados exitosamente.") 
    limpiar_campos()
    llenar_tablas_viajes()
    actualizar_tabla_vehiculos()
    
def actualizar_tabla_vehiculos():
    for row in tabla_vehiculos.get_children():
        tabla_vehiculos.delete(row)
    for index, vehiculo in enumerate(arbol_vehiculos.obtener_todos_vehiculos()):
        if index % 2 == 0:
            tabla_vehiculos.insert("", "end", values=(vehiculo.placa, vehiculo.marca, vehiculo.modelo, vehiculo.precio_por_segundo), tags=('evenrow',))
        else:
            tabla_vehiculos.insert("", "end", values=(vehiculo.placa, vehiculo.marca, vehiculo.modelo, vehiculo.precio_por_segundo), tags=('oddrow',))

def seleccionar_fila_vehiculos(event):
    selected_items = tabla_vehiculos.selection()
    if selected_items:
        selected_item = selected_items[0]
        valores = tabla_vehiculos.item(selected_item, 'values')
        
        entry_placa.config(state='normal')
        entry_placa.delete(0, tk.END)
        entry_placa.insert(0, valores[0])
        entry_placa.config(state='readonly')
        
        entry_marca.delete(0, tk.END)
        entry_marca.insert(0, valores[1])
        entry_modelo.delete(0, tk.END)
        entry_modelo.insert(0, valores[2])
        entry_precio_por_segundo.delete(0, tk.END)
        entry_precio_por_segundo.insert(0, valores[3])

def imprimir_estructura_vehiculos():
    arbol_vehiculos.graficar("vehiculos_arbol_b")
    messagebox.showinfo("Éxito", "Estructura del árbol B generada exitosamente.")

#########################################################################################################################
# Funciones para interfaz vehículos

def obtener_mes_dia_aleatorio():
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)
    return mes, dia

def obtener_hora_aleatoria():
    hora = random.randint(0, 23)
    minuto = random.randint(0, 59)
    segundo = random.randint(0, 59)
    return f"{hora:02}:{minuto:02}:{segundo:02}"

def llenar_tablas_viajes():
    for tabla in [tabla_lugares_origen_viajes, tabla_lugares_destino_viajes, tabla_clientes_viajes, tabla_vehiculos_viajes]:
        for row in tabla.get_children():
            tabla.delete(row)
    
    lugares = lista_adyacencia.obtener_todos_lugares()
    for index, lugar in enumerate(lugares):
        if index % 2 == 0:
            tabla_lugares_origen_viajes.insert("", "end", values=(lugar,), tags=('evenrow',))
            tabla_lugares_destino_viajes.insert("", "end", values=(lugar,), tags=('evenrow',))
        else:
            tabla_lugares_origen_viajes.insert("", "end", values=(lugar,), tags=('oddrow',))
            tabla_lugares_destino_viajes.insert("", "end", values=(lugar,), tags=('oddrow',))
    
    clientes = lista_clientes.mostrar()
    for index, cliente in enumerate(clientes):
        if index % 2 == 0:
            tabla_clientes_viajes.insert("", "end", values=(cliente.dpi, cliente.nombres, cliente.apellidos), tags=('evenrow',))
        else:
            tabla_clientes_viajes.insert("", "end", values=(cliente.dpi, cliente.nombres, cliente.apellidos), tags=('oddrow',))    

    vehiculos = arbol_vehiculos.obtener_todos_vehiculos()
    for index, vehiculo in enumerate(vehiculos):
        if index % 2 == 0:
            tabla_vehiculos_viajes.insert("", "end", values=(vehiculo.placa, vehiculo.marca, vehiculo.precio_por_segundo), tags=('evenrow',))
        else:
            tabla_vehiculos_viajes.insert("", "end", values=(vehiculo.placa, vehiculo.marca, vehiculo.precio_por_segundo), tags=('oddrow',))

def obtener_datos_seleccionados():    
    selected_items = tabla_lugares_origen_viajes.selection()
    if selected_items:
        origen = tabla_lugares_origen_viajes.item(selected_items[0], 'values')[0]

    selected_items = tabla_lugares_destino_viajes.selection()
    if selected_items:
        destino = tabla_lugares_destino_viajes.item(selected_items[0], 'values')[0]

    selected_items = tabla_clientes_viajes.selection()
    if selected_items:
        cliente = tabla_clientes_viajes.item(selected_items[0], 'values')

    selected_items = tabla_vehiculos_viajes.selection()
    if selected_items:
        vehiculo = tabla_vehiculos_viajes.item(selected_items[0], 'values')

    return origen, destino, cliente, vehiculo

def agregar_viaje():
    origen, destino, cliente, vehiculo = obtener_datos_seleccionados()

    if not origen or not destino or not cliente or not vehiculo:
        messagebox.showerror("Error", "Debe seleccionar un lugar de origen, un lugar de destino, un cliente y un vehículo.")
        return

    dpi_cliente = cliente[0]
    placa_vehiculo = vehiculo[0]

    mes, dia = obtener_mes_dia_aleatorio()
    hora = obtener_hora_aleatoria()
    fecha = f"{dia:02}/{mes:02}/2024"
    viaje = Viaje(origen, destino, fecha, hora, dpi_cliente, placa_vehiculo)
    messagebox.showinfo("Éxito", "Viaje registrado exitosamente.")
    mostrar_ruta_corta()

def seleccionar_fila_lugares_origen(event):
    selected_items = tabla_lugares_origen_viajes.selection()
    if selected_items:
        selected_item = selected_items[0]
        valores = tabla_lugares_origen_viajes.item(selected_item, 'values')
        entry_origen_viajes.config(state='normal')
        entry_origen_viajes.delete(0, tk.END)
        entry_origen_viajes.insert(0, valores[0])
        entry_origen_viajes.config(state='readonly')

def seleccionar_fila_lugares_destino(event):
    selected_items = tabla_lugares_destino_viajes.selection()
    if selected_items:
        selected_item = selected_items[0]
        valores = tabla_lugares_destino_viajes.item(selected_item, 'values')
        entry_destino_viajes.config(state='normal')
        entry_destino_viajes.delete(0, tk.END)
        entry_destino_viajes.insert(0, valores[0])
        entry_destino_viajes.config(state='readonly')

def seleccionar_fila_clientes(event):
    selected_items = tabla_clientes_viajes.selection()
    if selected_items:
        selected_item = selected_items[0]
        valores = tabla_clientes_viajes.item(selected_item, 'values')
        entry_dpi_viajes.config(state='normal')
        entry_dpi_viajes.delete(0, tk.END)
        entry_dpi_viajes.insert(0, valores[0])
        entry_dpi_viajes.config(state='readonly')

def seleccionar_fila_vehiculos(event):
    selected_items = tabla_vehiculos_viajes.selection()
    if selected_items:
        selected_item = selected_items[0]
        valores = tabla_vehiculos_viajes.item(selected_item, 'values')
        entry_placa_viajes.config(state='normal')
        entry_placa_viajes.delete(0, tk.END)
        entry_placa_viajes.insert(0, valores[0])
        entry_placa_viajes.config(state='readonly')

#########################################################################################################################

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
window_width = 1400
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
btn_imprimit_estructura_clientes = tk.Button(frame_botones_clientes, text="Imprimir Estructura - Clientes", command=imprimir_estructura_clientes, bg="#FFF2C2", fg="black")
btn_imprimit_estructura_clientes.pack(side=tk.LEFT, padx=5)

btn_carga_masiva = tk.Button(frame_botones_clientes, text="Carga Masiva - Clientes", command=cargar_clientes, bg="#FFF2C2", fg="black")
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
entry_dpi = tk.Entry(frame_campos_clientes, width=60)
entry_dpi.grid(row=0, column=1, pady=25)

tk.Label(frame_campos_clientes, text="Nombres:", bg="white").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_nombres = tk.Entry(frame_campos_clientes, width=60)
entry_nombres.grid(row=1, column=1, pady=25)

tk.Label(frame_campos_clientes, text="Apellidos:", bg="white").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_apellidos = tk.Entry(frame_campos_clientes, width=60)
entry_apellidos.grid(row=2, column=1, pady=25)

tk.Label(frame_campos_clientes, text="Género:", bg="white").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_genero = tk.Entry(frame_campos_clientes, width=60)
entry_genero.grid(row=3, column=1, pady=25)

tk.Label(frame_campos_clientes, text="Teléfono:", bg="white").grid(row=4, column=0, sticky=tk.W, pady=5)
entry_telefono = tk.Entry(frame_campos_clientes, width=60)
entry_telefono.grid(row=4, column=1, pady=25)

tk.Label(frame_campos_clientes, text="Dirección:", bg="white").grid(row=5, column=0, sticky=tk.W, pady=5)
entry_direccion = tk.Entry(frame_campos_clientes, width=60)
entry_direccion.grid(row=5, column=1, pady=25)

# Crear un frame contenedor para la tabla en la pestaña de clientes
frame_tabla_clientes = tk.Frame(tab_clientes, bg="white")
frame_tabla_clientes.pack(side=tk.LEFT, expand=True, fill='both', padx=20, pady=20)

# Crear la tabla
tabla_clientes = ttk.Treeview(frame_tabla_clientes, columns=("DPI", "Nombres", "Apellidos", "Género", "Teléfono", "Dirección"), show='headings')
tabla_clientes.heading("DPI", text="DPI")
tabla_clientes.heading("Nombres", text="Nombres")
tabla_clientes.heading("Apellidos", text="Apellidos")
tabla_clientes.heading("Género", text="Género")
tabla_clientes.heading("Teléfono", text="Teléfono")
tabla_clientes.heading("Dirección", text="Dirección")

tabla_clientes.column("DPI", width=100)
tabla_clientes.column("Nombres", width=150)
tabla_clientes.column("Apellidos", width=150)
tabla_clientes.column("Género", width=100)
tabla_clientes.column("Teléfono", width=100)
tabla_clientes.column("Dirección", width=200)

tabla_clientes.tag_configure('oddrow', background='white')
tabla_clientes.tag_configure('evenrow', background='#D4EBF8')

tabla_clientes.pack(expand=True, fill='both')

# Vincular el evento de selección de la tabla a la función seleccionar_fila
tabla_clientes.bind("<<TreeviewSelect>>", seleccionar_fila_clientes)

#########################################################################################################################

# Crear un frame contenedor para los botones en la parte superior de la pestaña de Vehiculos
frame_botones_container_vehiculos = tk.Frame(tab_vehiculos, bg="white")
frame_botones_container_vehiculos.pack(side=tk.TOP, fill=tk.X, pady=10)

frame_botones_vehiculos = tk.Frame(frame_botones_container_vehiculos, bg="white")
frame_botones_vehiculos.pack(expand=True)

# Añadir botones para las acciones de vehiculos
btn_imprimit_estructura_vehiculos = tk.Button(frame_botones_vehiculos, text="Imprimir Estructura - Vehiculos", command=imprimir_estructura_vehiculos, bg="#FFF2C2", fg="black")
btn_imprimit_estructura_vehiculos.pack(side=tk.LEFT, padx=5)

btn_carga_masiva = tk.Button(frame_botones_vehiculos, text="Carga Masiva - Vehiculos", command=cargar_vehiculos, bg="#FFF2C2", fg="black")
btn_carga_masiva.pack(side=tk.LEFT, padx=5)

btn_agregar_vehiculo = tk.Button(frame_botones_vehiculos, text="Agregar Vehiculo", command=agregar_vehiculo, bg="#FFF2C2", fg="black")
btn_agregar_vehiculo.pack(side=tk.LEFT, padx=5)

btn_modificar_vehiculo = tk.Button(frame_botones_vehiculos, text="Modificar Vehiculo", command=modificar_vehiculo, bg="#FFF2C2", fg="black")
btn_modificar_vehiculo.pack(side=tk.LEFT, padx=5)

btn_eliminar_vehiculo = tk.Button(frame_botones_vehiculos, text="Eliminar Vehiculo", command=eliminar_vehiculo, bg="#FFF2C2", fg="black")
btn_eliminar_vehiculo.pack(side=tk.LEFT, padx=5)

btn_limpiar_campos_vehiculo = tk.Button(frame_botones_vehiculos, text="Limpiar Campos", command=limpiar_campos, bg="#FFF2C2", fg="black")
btn_limpiar_campos_vehiculo.pack(side=tk.LEFT, padx=5)

# Crear un frame contenedor para los campos de entrada en la pestaña de vehiculos
frame_campos_vehiculos = tk.Frame(tab_vehiculos, bg="white")
frame_campos_vehiculos.pack(side=tk.RIGHT, expand=True, fill='both', padx=20, pady=20)

# Añadir campos de entrada para los datos del vehiculos
tk.Label(frame_campos_vehiculos, text="Placa:", bg="white").grid(row=0, column=0, sticky=tk.W, pady=5)
entry_placa = tk.Entry(frame_campos_vehiculos, width=60)
entry_placa.grid(row=0, column=1, pady=25, padx=10)

tk.Label(frame_campos_vehiculos, text="Marca:", bg="white").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_marca = tk.Entry(frame_campos_vehiculos, width=60)
entry_marca.grid(row=1, column=1, pady=25, padx=10)

tk.Label(frame_campos_vehiculos, text="Modelo:", bg="white").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_modelo = tk.Entry(frame_campos_vehiculos, width=60)
entry_modelo.grid(row=2, column=1, pady=25, padx=10)

tk.Label(frame_campos_vehiculos, text="Precio Por Segundo:", bg="white").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_precio_por_segundo = tk.Entry(frame_campos_vehiculos, width=60)
entry_precio_por_segundo.grid(row=3, column=1, pady=25, padx=10)

# Crear un frame contenedor para la tabla en la pestaña de vehiculos
frame_tabla_vehiculos = tk.Frame(tab_vehiculos, bg="white")
frame_tabla_vehiculos.pack(side=tk.LEFT, expand=True, fill='both', padx=20, pady=20)

# Crear la tabla - Vehiculos
tabla_vehiculos = ttk.Treeview(frame_tabla_vehiculos, columns=("Placa", "Marca", "Modelo", "Precio Por Segundo"), show='headings')
tabla_vehiculos.heading("Placa", text="Placa")
tabla_vehiculos.heading("Marca", text="Marca")
tabla_vehiculos.heading("Modelo", text="Modelo")
tabla_vehiculos.heading("Precio Por Segundo", text="Precio Por Segundo")

tabla_vehiculos.column("Placa", width=100)
tabla_vehiculos.column("Marca", width=150)
tabla_vehiculos.column("Modelo", width=150)
tabla_vehiculos.column("Precio Por Segundo", width=100)

tabla_vehiculos.tag_configure('oddrow', background='white')
tabla_vehiculos.tag_configure('evenrow', background='#D4EBF8')

tabla_vehiculos.pack(expand=True, fill='both')

# Vincular el evento de selección de la tabla a la función seleccionar_fila
tabla_vehiculos.bind("<<TreeviewSelect>>", seleccionar_fila_vehiculos)

#########################################################################################################################

# Crear un frame contenedor para las tablas en la pestaña de viajes
frame_tablas_viajes = tk.Frame(tab_viajes, bg="white")
frame_tablas_viajes.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Crear un frame contenedor para los campos de entrada y los botones en la pestaña de viajes
frame_viajes = tk.Frame(tab_viajes, bg="white")
frame_viajes.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Crear las tablas
tabla_lugares_origen_viajes = ttk.Treeview(frame_tablas_viajes, columns=("Lugar"), show='headings')
tabla_lugares_origen_viajes.heading("Lugar", text="Lugar de Origen")
tabla_lugares_origen_viajes.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
tabla_lugares_origen_viajes.column("Lugar", width=100)

tabla_lugares_origen_viajes.tag_configure('oddrow', background='white')
tabla_lugares_origen_viajes.tag_configure('evenrow', background='#D4EBF8')

tabla_lugares_destino_viajes = ttk.Treeview(frame_tablas_viajes, columns=("Lugar"), show='headings')
tabla_lugares_destino_viajes.heading("Lugar", text="Lugar de Destino")
tabla_lugares_destino_viajes.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
tabla_lugares_destino_viajes.column("Lugar", width=100)

tabla_lugares_destino_viajes.tag_configure('evenrow', background='white')
tabla_lugares_destino_viajes.tag_configure('oddrow', background='#D4EBF8')

tabla_clientes_viajes = ttk.Treeview(frame_tablas_viajes, columns=("DPI", "Nombres", "Apellidos"), show='headings')
tabla_clientes_viajes.heading("DPI", text="DPI")
tabla_clientes_viajes.heading("Nombres", text="Nombres")
tabla_clientes_viajes.heading("Apellidos", text="Apellidos")
tabla_clientes_viajes.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
tabla_clientes_viajes.column("DPI", width=100)
tabla_clientes_viajes.column("Nombres", width=150)
tabla_clientes_viajes.column("Apellidos", width=150)

tabla_clientes_viajes.tag_configure('oddrow', background='white')
tabla_clientes_viajes.tag_configure('evenrow', background='#D4EBF8')

tabla_vehiculos_viajes = ttk.Treeview(frame_tablas_viajes, columns=("Placa", "Marca", "Precio por Segundo"), show='headings')
tabla_vehiculos_viajes.heading("Placa", text="Placa")
tabla_vehiculos_viajes.heading("Marca", text="Marca")
tabla_vehiculos_viajes.heading("Precio por Segundo", text="Precio por Segundo")
tabla_vehiculos_viajes.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
tabla_vehiculos_viajes.column("Placa", width=80)
tabla_vehiculos_viajes.column("Marca", width=150)
tabla_vehiculos_viajes.column("Precio por Segundo", width=120)
tabla_vehiculos_viajes.tag_configure('oddrow', background='white')
tabla_vehiculos_viajes.tag_configure('evenrow', background='#D4EBF8')

# Campos de entrada
tk.Label(frame_viajes, text="Lugar de Origen:", bg="white").grid(row=0, column=0, sticky=tk.W, pady=5)
entry_origen_viajes = tk.Entry(frame_viajes, width=50)
entry_origen_viajes.grid(row=0, column=1, pady=5)

tk.Label(frame_viajes, text="Lugar de Destino:", bg="white").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_destino_viajes = tk.Entry(frame_viajes, width=50)
entry_destino_viajes.grid(row=1, column=1, pady=5)

tk.Label(frame_viajes, text="DPI del Cliente:", bg="white").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_dpi_viajes = tk.Entry(frame_viajes, width=50)
entry_dpi_viajes.grid(row=2, column=1, pady=5)

tk.Label(frame_viajes, text="Placa del Vehículo:", bg="white").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_placa_viajes = tk.Entry(frame_viajes, width=50)
entry_placa_viajes.grid(row=3, column=1, pady=5)

# Botón para encontrar la ruta más corta y registrar el viaje
btn_agregar_viaje = tk.Button(frame_viajes, text="Agregar Viaje", command=agregar_viaje, bg="#FFF2C2", fg="black")
btn_agregar_viaje.grid(row=4, columnspan=2, pady=10)

#########################################################################################################################
# Establecer el estilo para el fondo blanco de las pestañas
style = ttk.Style()
style.configure('TFrame', background='white')

# Crear el panel para la imagen en la pestaña de grafo
panel = tk.Label(tab_grafo, bg="white")
panel.pack(expand=True, fill='both')

# Vincular el evento de cambio de tamaño de la ventana a la función mostrar_imagen
tab_grafo.bind("<Configure>", mostrar_imagen)
tab_viajes.bind("<Configure>", llenar_tablas_viajes)

# Vincular el evento de selección de la tabla a la función seleccionar_fila
tabla_lugares_origen_viajes.bind("<<TreeviewSelect>>", seleccionar_fila_lugares_origen)
tabla_lugares_destino_viajes.bind("<<TreeviewSelect>>", seleccionar_fila_lugares_destino)
tabla_clientes_viajes.bind("<<TreeviewSelect>>", seleccionar_fila_clientes)
tabla_vehiculos_viajes.bind("<<TreeviewSelect>>", seleccionar_fila_vehiculos)

#cargar_datos_prueba()
actualizar_tabla_clientes()
actualizar_tabla_vehiculos()
llenar_tablas_viajes()

# Iniciar el bucle principal de la aplicación
root.mainloop()