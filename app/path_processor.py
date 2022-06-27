import osmnx as ox
import networkx as nx
from utils import *
import folium

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
    origin_node = ox.nearest_nodes(self.bicycle_graph, origin_location_coordinates[1], origin_location_coordinates[0])
    dest_node = ox.nearest_nodes(self.bicycle_graph, dest_location_coordinates[1], dest_location_coordinates[0])

    self.start_marker = folium.Marker(
            location = origin_location_coordinates,
            popup = origin_node,
            icon = folium.Icon(color='beige'))

    self.end_marker = folium.Marker(
            location = dest_location_coordinates,
            popup = dest_node,
            icon = folium.Icon(color='beige'))

    graph_aux = nx.DiGraph(self.bicycle_graph)

    if origin_node not in graph_aux or dest_node not in graph_aux:
      print("Point is not in graph")
      raise Exception("Change points")

    else:
      result = shortest_path(graph_aux, origin_node, dest_node, weight=optimizer)
      print(f"Everything ok: {result}")

    print(f"About to obtain paths from {origin_node} to {dest_node}...")
    shortest_routes = k_shortest_paths(graph_aux, origin_node, dest_node, N_PATHS, weight=optimizer)

    print(f"About to process {len(shortest_routes)} paths...")

    n = criteria_comparator.get_max_IC()
    best_routes = self.__get_best_route(shortest_routes, n, criteria_comparator)
    limit = get_limit(N_PATHS)
    print(f"Limit: {limit}")
    while (len(best_routes) != limit):
      if (len(best_routes) < limit):
        print("This shouldn't happen")
        raise Exception("Change points")
      best_routes = self.__get_best_route(best_routes, n, criteria_comparator)

    return self.__sort_best_routes(best_routes, criteria_comparator, limit)

  def get_markers(self):
    return (self.start_marker, self.end_marker)
    
  def __sort_best_routes(self, best_routes, criteria_comparator, n): 
    compared_alternatives = self.__get_compared_alternatives(criteria_comparator, best_routes)
    best_routes_sorted = criteria_comparator.get_best_routes(compared_alternatives, n)
    results = []
    for idx in best_routes_sorted:
      results.append(best_routes[idx])
    return results

  def __get_best_route(self, routes: List[List[int]], n, criteria_comparator) -> List[List[int]]:
    alternatives = [routes[i:i + n] for i in range(0, len(routes), n)]

    best_routes = []

    for alternative in alternatives:
      best_routes.append(self.__choose_route(alternative, criteria_comparator))

    return best_routes
 
  def __choose_route(self, alternatives: List[List[int]], criteria_comparator) -> List[int]: 
    if (len(alternatives) == 1): 
      return alternatives[0]

    compared_alternatives = self.__get_compared_alternatives(criteria_comparator, alternatives)

    best_route = criteria_comparator.get_best_route(compared_alternatives)

    return alternatives[best_route]

  def __get_compared_alternatives(self, criteria_comparator, alternatives):
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

    return compared_alternatives
