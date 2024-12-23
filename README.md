# Proyecto 1 | Rapidito 🏃‍♂️

## Objetivos
### Objetivo General
- Aplicar los conocimientos del curso de Estructuras de Datos en la creación de soluciones de software.
### Objetivos Específicos
- Aplicar los conocimientos adquiridos sobre estructuras de datos lineales y no lineales, árboles, grafos.
- Aplicar los conocimientos adquiridos sobre memoria dinámica y apuntadores en el lenguaje de programación Python.
- Utilizar la herramienta graphviz para la generación de reportes gráficos.

## Llega Rapidito
La empresa Llega Rapidito, durante varios años ha prestado su servicio de transporte con cobertura en todo el país.
Los directores de la compañía han decidido realizar un cambio de sistema para el control de vehículos, clientes y viajes, ya que el sistema actual cuenta con varios fallos y últimamente algunos procesos trabajan de forma lenta, esto debido a la gran cantidad de registros que maneja la empresa.
Por lo que se le ha contratado a usted para el desarrollo de una nueva solución, esta contará con una aplicación que estará implementada con estructuras de datos en memoria, esto con el propósito de agilizar los procesos utilizados para el control de la información.
## Aplicación
Aplicación deberá ser desarrollada en lenguaje de programación Python de forma gráfica. Por medio de esta aplicación se realizará el control de toda la información de interés para la empresa.
## Control de Información
El sistema debe manejar registros de las siguientes entidades:
- Clientes
- Vehículos
- Viajes
- Rutas

**Para cada entidad se deben realizar las siguientes operaciones:**
- Agregar
- Modificar (Ingresando llave)
- Eliminar (Ingresando llave)
- Mostrar Información (Ingresando llave)
- Mostrar Estructura de Datos (Graphviz)

## Clientes
La empresa desea tener registro de sus clientes, para la aplicación de descuentos y promociones, para los clientes se maneja la siguiente información:
- DPI
- Nombres
- Apellidos
- Género
- Teléfono
- Dirección
El control de clientes, estos se almacenarán en una Lista Circular Doblemente Enlazada, ordenada por el DPI.

### Carga Masiva de Clientes:
La aplicación debe contar con la opción para realizar la carga masiva de clientes por medio de un archivo de texto con el siguiente formato:
```
DPI, Nombres, Apellidos, Género, Teléfono, Dirección;
```

## Vehículos
Para los vehículos se utilizará la siguiente información:
- Placa
- Marca
- Modelo
- Precio por segundo (en quetzales)
Los vehículos se almacenarán en un árbol B de orden 5, utilizando como llave la placa de cada vehículo.

### Carga Masiva de Vehículos
La aplicación debe contar con la opción para realizar la carga masiva de vehículos por medio de un archivo de texto con el siguiente formato:
```
Placa : Marca : Modelo : Precio;
```

## Rutas
Al iniciar la aplicación, se deberá pedir la carga de un archivo el cuál contendrá las rutas de un país, en el archivo de proporcionará:
- Origen
- Destino
- Tiempo de Ruta
Por lo que se deberá ir realizando un mapa general de todas las rutas, implementado como un grafo que será implementado por el método de listas de adyacencia

### Carga de Rutas
Las rutas se cargarán al iniciar la aplicación, por medio de un archivo de texto con el siguiente formato:
```
Lugar Origen / Lugar Destino / Tiempo de Ruta %
```
Cada lugar tiene un nombre único, y el tiempo de ruta será proporcionado en segundos, proporcionados únicamente como números enteros.
Ejemplo:
```
Oviedo / Bilbao / 304 % 
Bilbao / Zaragoza / 324 % 
Bilbao / Madrid / 395 % 
Bilbao / Valladolid / 280 % 
Zaragoza / Barcelona / 296 % 
Barcelona / Gerona / 100 % 
Zaragoza / Madrid / 325 % …
```

## Viajes
Para cada viaje se tendrá la siguiente información y serán almacenado sen una Lista Simple:
- Lugar de Origen
- Lugar Destino
- Fecha y Hora de Inicio
- Cliente (Apuntador a Lista Circular)
- Vehículo (Apuntador a árbol B)
- Ruta Tomada. (Apuntador a Lista Simple)
El programa debe ser capaz de determinar el mejor camino por tomar, basándose en el grafo generado con el archivo cargado de rutas, y guardando en una lista simple, la ruta tomada, cada nodo debe tener: Nombre del lugar, Enlace al siguiente lugar, y Tiempo de llegada.

# Reportes
Serán generados en la aplicación por medio de la herramienta graphviz.
- **Top Viajes:** Top 5 de viajes más largos (por número de destinos).
- **Top Ganancia:** Top 5 de viajes más caros (por tiempo).
- **Top Clientes: **Top 5 de clientes con mayor cantidad de viajes.
- **Top Vehículos:** Top 5 de vehículos con mayor cantidad de viajes.
- **Ruta de un viaje** (Ingresando llave)
**Nota: Los reportes de tipo TOP deberán mostrarse en la aplicación en una tabla.**

## Flujo de la Aplicación
Básicamente el sistema tendrá el siguiente flujo:
- Al iniciar la aplicación se cargará el archivo de rutas, generando el grafo del cual se obtendrán las rutas más eficientes para los viajes.
- Se podrán realizar cargas masivas de:
    - Clientes
    - Vehículos
- Se debe tener un menú por cada entidad (Clientes, Vehículos, Viajes) Cada menú contara con la opción de:
    - Crear
    - Modificar (Ingresando llave)
    - Eliminar (Ingresando llave)
    - Mostrar Información (Ingresando llave)
    - Mostrar Estructura de Datos (Graphviz)
    - A excepción de los viajes de los cuáles se podrán aplicar únicamente las siguientes operaciones:
    - Crear
    - Mostrar Estructura de Datos (Graphviz)
- Se podrán generar Reportes.

# Entregables
- Ejecutable
- Código Fuente
- Manual de Usuario
- Manual Técnico

# Observaciones
- Lenguaje de Programación: Python
- Sistema Operativo: Elección del estudiante
- Herramienta de GUI: Elección del estudiante
- Las estructuras de datos deben ser realizadas por el estudiante.
- Fecha de Entrega y Calificación: Lunes 30 de diciembre antes de las 09:00 horas.
- Las gráficas deben mostrarse dentro de la aplicación, no buscarse en carpetas ajenas.
- Entrega en plataforma UEDI.
- Copias tendrán nota de 0 puntos y serán reportadas al catedrático y a la escuela de sistemas.