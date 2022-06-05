import osmnx as ox
import networkx as nx
from utils import *

N_PATHS = 1000

class PathProcessor:
  def __init__(self, bicycle_graph, cycleway_graph, surface_graph):
    self.bicycle_graph = bicycle_graph
    self.cycleway_graph = cycleway_graph
    self.surface_graph = surface_graph

  def get_paths(self, origin, destination, criteria_comparator):
    optimizer = criteria_comparator.get_optimizer()

    origin_location_coordinates = get_coordinates(origin)
    dest_location_coordinates = get_coordinates(destination)

    # Using bicycle_graph since it's the most complete graph
    # It should always be possible to obtain a path
    origin_node = ox.get_nearest_node(self.bicycle_graph, origin_location_coordinates)
    dest_node = ox.get_nearest_node(self.bicycle_graph, dest_location_coordinates)

    graph_aux = nx.DiGraph(self.bicycle_graph)
    print("About to obtain paths...")
    shortest_routes = k_shortest_paths(graph_aux, origin_node, dest_node, N_PATHS, weight=optimizer)

    n = criteria_comparator.get_max_IC()
    best_routes = self.__get_best_route(shortest_routes, n, criteria_comparator)
    while (len(best_routes) != 2):
      best_routes = self.__get_best_route(best_routes, n, criteria_comparator)
    
    return best_routes

  def __get_best_route(self, routes: List[List[int]], n, criteria_comparator) -> List[List[int]]:
    alternatives = [routes[i:i + n] for i in range(0, len(routes), n)]

    best_routes = []

    for alternative in alternatives:
      best_routes.append(self.__choose_route(alternative, criteria_comparator))

    return best_routes
 
  def __choose_route(self, alternatives: List[List[int]], criteria_comparator) -> List[int]: 
    if (len(alternatives) == 1): 
      return alternatives[0]

    compared_alternatives = []

    if criteria_comparator.is_criteria("cycleway"):
      cycleway_comparisons = process_comparisons(self.cycleway_graph, alternatives, calculate_graph_comparison)
      compared_alternatives.append(criteria_comparator.compare_alternative(cycleway_comparisons, "cycleway"))

    if criteria_comparator.is_criteria("surface"):
      surface_comparisons = process_comparisons(self.surface_graph, alternatives, calculate_graph_comparison)
      compared_alternatives.append(criteria_comparator.compare_alternative(surface_comparisons, "surface"))

    if criteria_comparator.is_criteria("length"):
      length_comparisons = process_comparisons(self.bicycle_graph, alternatives, calculate_measurable_comparison, 'length')
      compared_alternatives.append(criteria_comparator.compare_alternative(length_comparisons, "length"))

    if criteria_comparator.is_criteria("travel_time"):
      time_comparisons = process_comparisons(self.bicycle_graph, alternatives, calculate_measurable_comparison, 'travel_time')
      compared_alternatives.append(criteria_comparator.compare_alternative(time_comparisons, "travel_time"))

    best_route = criteria_comparator.get_best_route(compared_alternatives)

    return alternatives[best_route]