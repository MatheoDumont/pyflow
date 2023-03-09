from . import workflow
from .graph.vertex import Vertex


class Process(Vertex):
    def __init__(self, *args, **kwargs):
        super().__init__()
        workflow.add_process(self)

        for arg in args:
            if type(args) is Process:
                pass
            elif :
                pass # create process from value 

        