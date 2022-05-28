import osmnx as ox
import networkx as nx
from utils import *

N_PATHS = 1000

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
    print("About to obtain paths...")
    shortest_routes = k_shortest_paths(graph_aux, origin_node, dest_node, N_PATHS, weight=optimizer)

    print("About to create html...")
    '''for i in range(len(shortest_routes)):
      shortest_route_map = ox.plot_route_folium(self.bicycle_graph, shortest_routes[i])
      shortest_route_map.save(str(i) + "cycleway.html")'''

    n = self.criteria_comparator.get_max_IC()
    best_routes = self.__get_best_route(shortest_routes, n)
    while (len(best_routes) != 1):
      best_routes = self.__get_best_route(best_routes, n)
    
    return best_routes[0]

  def __get_best_route(self, routes: List[List[int]], n) -> List[List[int]]:
    alternatives = [routes[i:i + n] for i in range(0, len(routes), n)]

    best_routes = []

    for alternative in alternatives:
      best_routes.append(self.__choose_route(alternative))

    return best_routes
 
  def __choose_route(self, alternatives: List[List[int]]) -> List[int]: 
    if (len(alternatives) == 1): 
      return alternatives[0]

    compared_alternatives = []

    if self.criteria_comparator.is_criteria("cycleway"):
      cycleway_comparisons = process_comparisons(self.cycleway_graph, alternatives, calculate_graph_comparison)
      compared_alternatives.append(self.criteria_comparator.compare_alternative(cycleway_comparisons, "cycleway", len(alternatives)))

    if self.criteria_comparator.is_criteria("surface"):
      surface_comparisons = process_comparisons(self.surface_graph, alternatives, calculate_graph_comparison)
      compared_alternatives.append(self.criteria_comparator.compare_alternative(surface_comparisons, "surface", len(alternatives)))

    if self.criteria_comparator.is_criteria("length"):
      length_comparisons = process_comparisons(self.bicycle_graph, alternatives, calculate_measurable_comparison, 'length')
      compared_alternatives.append(self.criteria_comparator.compare_alternative(length_comparisons, "length", len(alternatives)))

    if self.criteria_comparator.is_criteria("travel_time"):
      time_comparisons = process_comparisons(self.bicycle_graph, alternatives, calculate_measurable_comparison, 'travel_time')
      compared_alternatives.append(self.criteria_comparator.compare_alternative(time_comparisons, "travel_time", len(alternatives)))

    best_route = self.criteria_comparator.get_best_route(compared_alternatives)

    return alternatives[best_route]