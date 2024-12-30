# Manual Técnico

## Proyecto 1: Rapidito 🏃‍♂️

#### Introducción

El sistema Rapidito es una aplicación diseñada para optimizar la gestión de información en la empresa Llega Rapidito, utilizando estructuras de datos avanzadas y generación dinámica de reportes. Este manual técnico detalla la arquitectura del sistema, los componentes implementados, las tecnologías utilizadas y el flujo interno de la aplicación.

## Arquitectura del Sistema

El sistema está desarrollado en Python, utilizando estructuras de datos implementadas manualmente y un enfoque modular. La aplicación consta de los siguientes módulos principales:

### Módulos Principales

1. Gestor de Clientes

Implementado mediante una lista circular doblemente enlazada.

Funciones principales: agregar, modificar, eliminar, mostrar información, y visualizar estructura de datos.

2. de Vehículos

Utiliza un árbol B de orden 5 para almacenamiento eficiente.

Funciones principales: agregar, modificar, eliminar, mostrar información, y visualizar estructura de datos.

3. de Rutas

Implementado con grafos representados por listas de adyacencia.

Permite calcular rutas eficientes y gestionar el mapa de rutas.

4. de Viajes

Almacenamiento en una lista simple.

Incluye la capacidad de determinar la ruta más eficiente basada en el grafo de rutas cargado.

5. de Reportes

Utiliza la herramienta Graphviz para generar representaciones gráficas de las estructuras de datos y reportes visuales.

## Tecnologías Utilizadas

- Lenguaje de programación: Python.

- Interfaz Gráfica (GUI): Biblioteca seleccionada por el desarrollador (Tkinter, PyQt, o cualquier otra compatible).

- Herramienta de graficación: Graphviz.

- Sistema operativo: Compatible con Windows, macOS y Linux.

## Estructuras de Datos

### Lista Circular Doblemente Enlazada (Clientes)

#### Implementación

- Cada nodo contiene:

DPI, Nombres, Apellidos, Género, Teléfono, Dirección.

Enlaces al nodo anterior y siguiente.

#### Operaciones

Agregar: Inserta un nuevo nodo en orden ascendente por DPI.

Eliminar: Busca y elimina un nodo por DPI.

Modificar: Actualiza la información del cliente.

### Árbol B (Vehículos)

#### Implementación

Orden 5 (cada nodo puede tener hasta 4 claves y 5 hijos).

Llave principal: Placa del vehículo.

#### Operaciones

Inserción: Ajusta las claves y nodos según sea necesario.

Borrado: Redistribuye claves o fusiona nodos.

Búsqueda: Recupera la información del vehículo.

### Grafo (Rutas)

#### Representación

Listas de adyacencia.

Cada nodo representa un lugar, y las aristas contienen el tiempo de ruta en segundos.

#### Operaciones

Carga inicial: Construye el grafo desde el archivo proporcionado.

Cálculo de rutas: Algoritmo de camino más corto (Dijkstra o similar).

### Lista Simple (Viajes)

#### Estructura

Cada nodo contiene:

Origen, Destino, Fecha y Hora de Inicio, Cliente, Vehículo, y Ruta Tomada.

#### Operaciones

Crear: Agrega un viaje nuevo.

Mostrar estructura: Visualiza la lista simple con Graphviz.

## Flujo de la Aplicación

1. Inicio

- Carga del archivo de rutas para inicializar el grafo.

2. Carga Masiva de Datos

- Opciones disponibles para clientes y vehículos.

3. Gestor de Entidades

- Menú por cada entidad con opciones para crear, modificar, eliminar y mostrar información.

4. Viajes

- Creación de viajes con selección de cliente, vehículo y cálculo de ruta más eficiente.

5. Generación de Reportes

- Tablas y gráficas para analizar viajes, clientes y vehículos.

## Reportes

### Tipos de Reportes

1. Top Viajes: Los 5 viajes con mayor número de destinos.

2. Top Ganancia: Los 5 viajes con mayor costo.

3. Top ClientesFlujo de la Aplicación

    1. Inicio

    - Carga del archivo de rutas para inicializar el grafo.

    2. Carga Masiva de Datos

    - Opciones disponibles para clientes y vehículos.

    3. Gestor de Entidades

    - Menú por cada entidad con opciones para crear, modificar, eliminar y mostrar información.

    4. Viajes

    - Creación de viajes con selección de cliente, vehículo y cálculo de ruta más eficiente.

    5. Generación de Reportes

    - Tablas y gráficas para analizar viajes, clientes y vehículos.

## : Clientes con más viajes realizados.

4. Top Vehículos: Vehículos utilizados con mayor frecuencia.

5. Ruta de un Viaje: Representación gráfica de la ruta tomada.

#### Generación

- Los reportes se crean dinámicamente y se visualizan en la aplicación.

## Requisitos del Sistema

- Lenguaje: Python 3.8 o superior.

- Librerías:

    - Graphviz.

    - Biblioteca para GUI (Tkinter, PyQt, etc.).

- Archivos de datos: Formatos especificados en el manual de usuario.

## Consideraciones

1. Verifique que los archivos de entrada sigan el formato correcto para evitar errores.

2. Los reportes deben visualizarse exclusivamente dentro de la aplicación.

3. Las estructuras de datos deben ser implementadas manualmente, sin usar librerías externas para estas.

** Nota: Para cualquier consulta o soporte técnico, comuníquese con el desarrollador encargado del proyecto.** 