from cycleway_graph_builder import *
from surface_graph_builder import *
from path_processor import *

surface_graph = SurfaceGraphBuilder().build()
PathProcessor(surface_graph).save_path("Julian Alvarez, 400, Buenos Aires", "Julian Alvarez, 800, Buenos Aires", "length", "surface.html")

cycleway_graph = CyclewayGraphBuilder().build()
PathProcessor(cycleway_graph).save_path("Julian Alvarez, 400, Buenos Aires", "Julian Alvarez, 800, Buenos Aires", "length", "cycleway.html")
