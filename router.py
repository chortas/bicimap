from cycleway_graph_builder import *
from path_processor import *

graph = CyclewayGraphBuilder().build()
PathProcessor(graph).save_path("Julian Alvarez, 400, Buenos Aires", "Julian Alvarez, 800, Buenos Aires", "length", "jaja.html")

