from cycleway_graph_builder import *
from surface_graph_builder import *
from bicycle_graph_builder import *
from path_processor import *
from criteria_comparator import *

'''
If a criteria is not relevant it isn't added to the initial comparisons.
If it is relevant, it should be compared with the rest.
Special case: length vs travel_time, the more relevant should be the weight to get the paths.
'''

comparison_criteria = ['cycleway', 'surface', 'travel_time']
comparisons = {('travel_time', 'surface'): 5, ('travel_time', 'cycleway'): 5, ('cycleway', 'surface'): 1}
criteria_comparator = CriteriaComparator(comparison_criteria)
criteria_comparator.compare_criteria(comparisons, 'Criteria')

bicycle_graph_builder = BicycleGraphBuilder()
bicycle_graph_builder.print()
bicycle_graph = bicycle_graph_builder.build()
cycleway_graph_builder = CyclewayGraphBuilder()
cycleway_graph_builder.print()
cycleway_graph = cycleway_graph_builder.build()
surface_graph_builder = SurfaceGraphBuilder()
surface_graph_builder.print()
surface_graph = surface_graph_builder.build()

path_processor = PathProcessor(bicycle_graph, cycleway_graph, surface_graph, criteria_comparator)
path = path_processor.get_path("Lavalleja, 840, Buenos Aires", "Acoyte, 235 Buenos Aires")
print(len(path))
shortest_route_map = ox.plot_route_folium(bicycle_graph, path)
shortest_route_map.save("cycleway.html")
