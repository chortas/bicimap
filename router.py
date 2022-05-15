from cycleway_graph_builder import *
from surface_graph_builder import *
from bicycle_graph_builder import *
from path_processor import *

surface_graph = SurfaceGraphBuilder().build()
bicycle_graph = BicycleGraphBuilder().build()
PathProcessor().save_path("Santos Dumont, 3294, Buenos Aires", "Santos Dumont, 3693, Buenos Aires", "length", "surface_test.html", surface_graph, bicycle_graph)

'''cycleway_graph = CyclewayGraphBuilder().build()
PathProcessor(cycleway_graph).save_path("Julian Alvarez, 400, Buenos Aires", "Julian Alvarez, 800, Buenos Aires", "length", "cycleway.html")'''
