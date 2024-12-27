from src.ListaSimple.ListaSimple import ListaSimple
from src.Clases.Vertices import Vertice
from src.Clases.Rutas import Ruta
from src.ListaSimple.Nodo import Nodo
import graphviz, os

class ListaAdyacencia:
    def __init__(self):
        self.vertices = ListaSimple()
        
    def insertar(self, origen, destino, tiempo):
        resultado = self.vertices.buscar(origen)
        
        if resultado is None:
            nuevo_vertice = Vertice(origen)
            nuevo_vertice.adyacentes.insertar(Ruta(origen, destino, tiempo))
            self.vertices.insertar(nuevo_vertice)
            return f"Vértice {origen} agregado con adyacente {destino} ({tiempo} min)."
        else:
            resultado.nombre.adyacentes.insertar(Ruta(origen, destino, tiempo))
            return f"Adyacente {destino} agregado al vértice {origen} ({tiempo} min)."

    def mostrar_grafo(self):
        actual = self.vertices.inicio
        grafo_str = ""
        while actual:
            vertice = actual.nombre
            adyacentes_str = ""
            adyacente_actual = vertice.adyacentes.inicio
            while adyacente_actual:
                ruta = adyacente_actual.nombre
                adyacentes_str += f"{ruta.destino} ({ruta.tiempo} min), "
                adyacente_actual = adyacente_actual.siguiente
            adyacentes_str = adyacentes_str.rstrip(", ")
            grafo_str += f"{vertice.nombre} -> {adyacentes_str}\n"
            actual = actual.siguiente
        print(grafo_str.strip())
        return grafo_str.strip()

    def eliminar_grafo(self):
        self.vertices = ListaSimple()
        return "Grafo eliminado."
    
    def graficar(self, filename="grafo"):
        dot = graphviz.Graph(comment='Grafo')
        actual = self.vertices.inicio
        while actual:
            vertice = actual.nombre
            dot.node(vertice.nombre)
            adyacente_actual = vertice.adyacentes.inicio
            while adyacente_actual:
                ruta = adyacente_actual.nombre
                dot.edge(vertice.nombre, ruta.destino, label=f"{ruta.tiempo}")
                adyacente_actual = adyacente_actual.siguiente
            actual = actual.siguiente
        
        output_dir = os.path.join(os.getcwd(), "Graphviz")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        base_filename = filename
        counter = 1
        ruta_grafo = os.path.join(output_dir, f"{base_filename}")
        while os.path.exists(ruta_grafo):
            ruta_grafo = os.path.join(output_dir, f"{base_filename}({counter})")
            counter += 1
        
        dot.render(ruta_grafo, format='png', cleanup=True)
        print(f"Grafo guardado como {ruta_grafo}")
        return ruta_grafo + ".png"
        
    def cargar_rutas_desde_contenido(self, contenido):
        for line in contenido.splitlines():
            line = line.strip().rstrip('%').strip()
            origen, destino, tiempo = line.split(' / ')
            tiempo = int(tiempo.split(' ')[0])
            self.insertar(origen, destino, tiempo)
        print("Rutas cargadas exitosamente desde el contenido.")
        print()