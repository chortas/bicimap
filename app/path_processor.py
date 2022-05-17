import osmnx as ox
import networkx as nx
from utils import *

N_PATHS = 2

class PathProcessor:
  def __init__(self, bicycle_graph, cycleway_graph, surface_graph, criteria_comparator):
    self.bicycle_graph = bicycle_graph
    self.cycleway_graph = cycleway_graph
    self.surface_graph = surface_graph
    self.criteria_comparator = criteria_comparator

  def get_path(self, origin, destination, optimizer):
    origin_location_coordinates = get_coordinates(origin)
    dest_location_coordinates = get_coordinates(destination)

    # Using bicycle_graph since it's the most complete graph
    # It should always be possible to obtain a path
    origin_node = ox.get_nearest_node(self.bicycle_graph, origin_location_coordinates)
    dest_node = ox.get_nearest_node(self.bicycle_graph, dest_location_coordinates)

    graph_aux = nx.DiGraph(self.bicycle_graph)
    shortest_routes = k_shortest_paths(graph_aux, origin_node, dest_node, N_PATHS, weight=optimizer)
    
    cycleway_comparisons = process_comparisons(self.cycleway_graph, shortest_routes)
    self.criteria_comparator.compare_alternative(cycleway_comparisons, "cycleway", N_PATHS)

    surface_comparisons = process_comparisons(self.surface_graph, shortest_routes)
    self.criteria_comparator.compare_alternative(surface_comparisons, "surface", N_PATHS)

    best_route = self.criteria_comparator.get_best_route()
    print(f"The best route given all comparions is: {best_route}")
    print(f"Route: shortest_routes{shortest_routes[best_route]}")

    return shortest_routes[best_route]
