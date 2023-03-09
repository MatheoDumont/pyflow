
from .graph.directed_acyclic_graph import DAG



class Workflow:

    def __init__(self):
        self.dag = DAG()

    def add_process(self, process):
        self.dag.add_vertex(process)