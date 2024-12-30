from src.Estructuras.ListaSimple.ListaSimple import ListaSimple
from src.Clases.Vertices import Vertice
from src.Clases.Rutas import Ruta
from src.Estructuras.Cola.Cola import Cola
from src.Estructuras.Cola.Nodo import Nodo
import graphviz, os
from copy import copy

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

    def buscar(self, origen):
        aux = self.vertices.inicio
        while aux is not None:
            if aux.nombre.nombre == origen:
                return aux.nombre
            aux = aux.siguiente
        return None
    
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
        dot = graphviz.Graph(engine='neato', comment='Grafo')
        
        dot.attr(fontsize='5')
        dot.attr('edge', len='3.0')
        
        actual = self.vertices.inicio
        visitados = set()
        while actual:
            vertice = actual.nombre
            adyacente_actual = vertice.adyacentes.inicio
            while adyacente_actual:
                ruta = adyacente_actual.nombre
                if (vertice.nombre, ruta.destino) not in visitados and (ruta.destino, vertice.nombre) not in visitados:
                    dot.edge(vertice.nombre, ruta.destino, label=f"{ruta.tiempo}")
                    visitados.add((vertice.nombre, ruta.destino))
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
        contenido = contenido.strip()
        
        lineas = contenido.split('\n')
        for linea in lineas:
            linea = linea.strip()
            
            if linea.endswith('%'):
                linea = linea[:-1]
                
                campos = linea.split('/')
                
                if len(campos) == 3:
                    origen, destino, distancia = campos
                    self.insertar(origen, destino, float(distancia))
                else:
                    print(f"Línea inválida: {linea}")
    
    def obtener_todos_lugares(self):
        lugares = []
        actual = self.vertices.inicio
        while actual:
            adyacente_actual = actual.nombre.adyacentes.inicio
            while adyacente_actual:
                ruta = adyacente_actual.nombre
                if ruta.destino not in lugares:
                    lugares.append(ruta.destino)
                    print(ruta.destino) 
                adyacente_actual = adyacente_actual.siguiente
            actual = actual.siguiente
        return lugares
    
    def obtener_rutas_desde(self, origen, destino) -> ListaSimple:
        ruta: ListaSimple[Vertice] = ListaSimple()
        nodos_visitados: Cola = Cola()
        nodos: Cola = Cola()
        
        original: Vertice = copy(self.buscar(origen))
        
        if original is None:
            print(f"No se encontró el lugar de origen: {origen}")
            return
        
        nodos.encolar(original)
        
        resultado: Vertice = self.get_ruta_corta(destino, nodos_visitados, nodos)
        while resultado is not None:
            ruta.insertar(resultado)
            resultado = resultado.padre

        return ruta

    def get_ruta_corta(self, destino, nodos_visitados: Cola, nodos: Cola) -> Vertice:
        if nodos.vacio():
            return None
        
        original: Vertice = nodos.desencolar().nombre
        
        if original.nombre == destino:
            nodos_visitados.encolar(original)
            return original
        
        aux: Nodo[Vertice] = original.adyacentes.inicio
        
        while aux is not None:
            if not self.es_visitado(nodos_visitados, aux.nombre.destino):
                tiempo: int = aux.nombre.tiempo  # Cambia 'peso' por 'tiempo'
                
                adyacente: Vertice = copy(self.buscar(aux.nombre.destino))
                adyacente.tiempo = tiempo  # Cambia 'peso' por 'tiempo'
                adyacente.set_peso_acumulado(original.peso_acumulado + tiempo)  # Cambia 'peso' por 'tiempo'
                adyacente.padre = original
                
                nodos.encolar(adyacente)
                
            aux = aux.siguiente
            
        nodos.ordenar()
        nodos_visitados.encolar(original)
        return self.get_ruta_corta(destino, nodos_visitados, nodos)

    def es_visitado(self, nodos_visitados: Cola, destino: str) -> bool:
        actual = nodos_visitados.inicio
        while actual is not None:
            if actual.nombre.nombre == destino:
                return True
            actual = actual.siguiente
        return False