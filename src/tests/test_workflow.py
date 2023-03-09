
from ..pyflow.process import Process
from ..pyflow import workflow

from .processes import Process1, Process2

p1 = Process1()
Process2(p1)


print(workflow.dag.vertices_edges)