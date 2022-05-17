from cycleway_graph_builder import *
from surface_graph_builder import *
from bicycle_graph_builder import *
from path_processor import *
from criteria_comparator import *

comparisons = {('cycleway', 'surface'): 9}
criteria_comparator = CriteriaComparator(comparisons, 2)
print(f"Is consistent?: {criteria_comparator.is_consistent()}")

'''
surface_graph = SurfaceGraphBuilder().build()
bicycle_graph = BicycleGraphBuilder().build()
PathProcessor().save_path("Santos Dumont, 3294, Buenos Aires", "Santos Dumont, 3693, Buenos Aires", "length", "surface_test.html", surface_graph, bicycle_graph)
'''

'''cycleway_graph = CyclewayGraphBuilder().build()
PathProcessor(cycleway_graph).save_path("Julian Alvarez, 400, Buenos Aires", "Julian Alvarez, 800, Buenos Aires", "length", "cycleway.html")'''
