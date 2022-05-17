from cycleway_graph_builder import *
from surface_graph_builder import *
from bicycle_graph_builder import *
from path_processor import *
from criteria_comparator import *

'''
If a criteria is not relevant it isn't added to the initial comparisons.
If it is relevant, it should be compared with the rest.
Special case: time vs length, the more relevant should be the weight to get the paths.
'''

comparison_criteria = ['cycleway', 'surface', 'length']
comparisons = {('cycleway', 'surface'): 5, ('cycleway', 'length'): 4, ('surface', 'length'): 3}
criteria_comparator = CriteriaComparator(comparison_criteria)
criteria_comparator.compare_criteria(comparisons, 'Criteria', 3)

bicycle_graph = BicycleGraphBuilder().build()
cycleway_graph = CyclewayGraphBuilder().build()
surface_graph = SurfaceGraphBuilder().build()

path_processor = PathProcessor(bicycle_graph, cycleway_graph, surface_graph, criteria_comparator)

path = path_processor.get_path("Santos Dumont, 3294, Buenos Aires", "Lavalleja, 701 Buenos Aires", "length")
shortest_route_map = ox.plot_route_folium(bicycle_graph, path)
shortest_route_map.save("cycleway.html")
