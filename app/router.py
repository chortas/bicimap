from cycleway_graph_builder import *
from surface_graph_builder import *
from bicycle_graph_builder import *
from path_processor import *
from criteria_comparator import *

comparisons = {('cycleway', 'surface'): 9}
criteria_comparator = CriteriaComparator()
criteria_comparator.compare_criteria(comparisons, 'Criteria', 2)

bicycle_graph = BicycleGraphBuilder().build()
cycleway_graph = CyclewayGraphBuilder().build()
surface_graph = SurfaceGraphBuilder().build()

path_processor = PathProcessor(bicycle_graph, cycleway_graph, surface_graph, criteria_comparator)

#PathProcessor().save_path("Santos Dumont, 3294, Buenos Aires", "Santos Dumont, 3693, Buenos Aires", "length", "surface_test.html")
path = path_processor.get_path("Julian Alvarez, 400, Buenos Aires", "Julian Alvarez, 800, Buenos Aires", "length")
shortest_route_map = ox.plot_route_folium(bicycle_graph, path)
shortest_route_map.save("cycleway.html")
