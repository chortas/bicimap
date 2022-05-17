import osmnx as ox
import networkx as nx
from utils import *

N_PATHS = 100

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

    for i in range(len(shortest_routes)):
      shortest_route_map = ox.plot_route_folium(self.bicycle_graph, shortest_routes[i])
      shortest_route_map.save(str(i) + "cycleway.html")
    
    if self.criteria_comparator.is_criteria("cycleway"):
      cycleway_comparisons = process_comparisons(self.cycleway_graph, shortest_routes, calculate_graph_comparison)
      self.criteria_comparator.compare_alternative(cycleway_comparisons, "cycleway", N_PATHS)

    if self.criteria_comparator.is_criteria("surface"):
      surface_comparisons = process_comparisons(self.surface_graph, shortest_routes, calculate_graph_comparison)
      self.criteria_comparator.compare_alternative(surface_comparisons, "surface", N_PATHS)

    if self.criteria_comparator.is_criteria("length"):
      length_comparisons = process_comparisons(self.bicycle_graph, shortest_routes, calculate_measurable_comparison)
      self.criteria_comparator.compare_alternative(length_comparisons, "length", N_PATHS)

    '''if self.criteria_comparator.is_criteria("time"):
      time_comparisons = process_comparisons(self.bicycle_graph, shortest_routes, calculate_measurable_comparison)
      self.criteria_comparator.compare_alternative(time_comparisons, "time", N_PATHS)'''

    best_route = self.criteria_comparator.get_best_route()
    print(f"The best route given all comparisons is: {best_route}")
    print(f"Route: shortest_routes{shortest_routes[best_route]}")

    return shortest_routes[best_route]
