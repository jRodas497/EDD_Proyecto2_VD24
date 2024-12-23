from src.ListaSimple.ListaSimple import ListaSimple
from src.Clases.Vertices import Vertice
import graphviz, os

class ListaAdyacencia:
    def __init__(self):
        self.vertices = ListaSimple()
        
    def insertar(self, origen, destino):
        resultado = self.vertices.buscar(origen)
        
        if resultado is None:
            nuevo_vertice = Vertice(origen)
            nuevo_vertice.adyacentes.insertar(destino)
            self.vertices.insertar(nuevo_vertice)
            return f"Vértice {origen} agregado con adyacente {destino}."
        else:
            resultado.adyacentes.insertar(destino)
            return f"Adyacente {destino} agregado al vértice {origen}."

    def mostrar_grafo(self):
        actual = self.vertices.inicio
        grafo_str = ""
        while actual:
            vertice = actual.nombre
            adyacentes_str = ""
            adyacente_actual = vertice.adyacentes.inicio
            while adyacente_actual:
                adyacentes_str += f"{adyacente_actual.nombre}, "
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
        dot = graphviz.Digraph(comment='Grafo')
        actual = self.vertices.inicio
        while actual:
            vertice = actual.nombre
            dot.node(vertice.nombre)
            adyacente_actual = vertice.adyacentes.inicio
            while adyacente_actual:
                dot.edge(vertice.nombre, adyacente_actual.nombre)
                adyacente_actual = adyacente_actual.siguiente
            actual = actual.siguiente
        dot.render(filename, format='png', cleanup=True)
        print(f"Grafo guardado como {filename}.png")