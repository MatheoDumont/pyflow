
from .vertex import Vertex


class DAG:
    """
    DAG: Directed Acyclic Graph
    """

    def __init__(self):
        self.vertices_edges = {}
        self.id_to_vertex = {}

    def add_vertex(self, vertex: Vertex) -> bool:
        if vertex.id in self.id_to_vertex:
            raise ValueError(f"Process with name '{vertex.id}' duplicate found!")

        self.vertices_edges[vertex.id] = []
        self.id_to_vertex[vertex.id] = vertex

        return True