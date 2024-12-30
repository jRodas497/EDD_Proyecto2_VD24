# Manual de Usuario

# Proyecto 1: Rapidito 🏃‍♂️

## Introducción

Bienvenido al sistema Rapidito, una aplicación desarrollada para la empresa Llega Rapidito que permite gestionar de manera eficiente la información relacionada con clientes, vehículos, rutas y viajes. Este manual tiene como objetivo guiar al usuario en la utilización de la aplicación y aprovechar al máximo sus funcionalidades.

## Objetivos

### Objetivo General

Aplicar los conocimientos de estructuras de datos para optimizar la gestión de información en Llega Rapidito.

### Objetivos Específicos

## Implementar estructuras de datos como listas, árboles y grafos.

Utilizar memoria dinámica y apuntadores en Python.

### Generar reportes gráficos utilizando la herramienta Graphviz.

## Instrucciones de Uso

Inicio de la Aplicación

Carga de rutas: Al iniciar, se cargará un archivo de texto con las rutas del país. Este archivo debe tener el formato:

Origen / Destino / Tiempo de Ruta %

## Ejemplo:

Oviedo / Bilbao / 304 %
Bilbao / Zaragoza / 324 %

Generación del Grafo: Con la información de rutas, se creará un grafo representado mediante listas de adyacencia.

## Carga Masiva de Datos

### Clientes

Seleccione la opción Cargar Clientes en el menú.

Ingrese un archivo de texto con el siguiente formato:

DPI, Nombres, Apellidos, Género, Teléfono, Dirección;

## Ejemplo:

123456789, Juan, Pérez, M, 55551234, Guatemala;

### Vehículos

Seleccione la opción Cargar Vehículos en el menú.

Ingrese un archivo de texto con el siguiente formato:

Placa : Marca : Modelo : Precio;

Ejemplo:

P123ABC : Toyota : Corolla : 0.5;

Gestión de Entidades

### Clientes

Agregar: Ingrese los datos del cliente manualmente en los campos correspondientes.

Modificar: Proporcione el DPI del cliente y actualice los campos deseados.

Eliminar: Ingrese el DPI del cliente que desea eliminar.

Mostrar Información: Busque un cliente ingresando su DPI.

Visualizar Estructura de Datos: Visualice la lista circular doblemente enlazada utilizando Graphviz.

### Vehículos

Agregar: Ingrese los datos del vehículo manualmente.

Modificar: Proporcione la placa del vehículo y actualice los campos deseados.

Eliminar: Ingrese la placa del vehículo que desea eliminar.

Mostrar Información: Busque un vehículo ingresando su placa.

Visualizar Estructura de Datos: Visualice el árbol B utilizando Graphviz.

### Rutas

Mostrar Grafo: Visualice el grafo generado a partir del archivo de rutas.

### Viajes

Crear: Ingrese los datos requeridos: origen, destino, fecha, cliente, vehículo y ruta tomada.

Visualizar Estructura de Datos: Visualice la lista simple de viajes utilizando Graphviz.

### Reportes

La aplicación genera los siguientes reportes:

Top Viajes: Los 5 viajes con mayor cantidad de destinos.

Top Ganancia: Los 5 viajes más caros (según el tiempo).

Top Clientes: Los 5 clientes con mayor cantidad de viajes.

Top Vehículos: Los 5 vehículos con mayor cantidad de viajes.

Ruta de un Viaje: Visualice la ruta tomada de un viaje ingresando su identificador.

Todos los reportes se muestran en formato de tabla dentro de la aplicación y algunos incluyen representaciones gráficas.

#### Observaciones

Lenguaje de programación: Python.

Sistema operativo: Compatible con cualquier sistema operativo.

Interfaz gráfica: Seleccionada por el desarrollador.

Entrega de reportes gráficos: Directamente en la aplicación.

Nota: Asegúrese de cumplir con el formato de archivos especificado para evitar errores en la carga de datos.

