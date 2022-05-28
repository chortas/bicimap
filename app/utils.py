from itertools import islice, combinations
from typing import Dict, List, Tuple
from geopy.geocoders import Nominatim
import osmnx as ox
import networkx as nx

def k_shortest_paths(G, source, target, k, weight=None) -> List[List[int]]:
  return list(islice(nx.shortest_simple_paths(G, source, target, weight=weight), k))

def get_coordinates(location):
  locator = Nominatim(user_agent = "BiciMap")
  location_geocoded = locator.geocode(location)
  return (location_geocoded.latitude, location_geocoded.longitude)

def calculate_graph_comparison(graph, route):
  n_edges = 0
  for u, v in zip(route, route[1:]):
    if graph.has_edge(u, v): n_edges += 1
  return n_edges / len(route)

def calculate_measurable_comparison(graph, route, parameter):
  measure = 0
  for u, v in zip(route, route[1:]):
    measure += graph.get_edge_data(u, v)[0][parameter]
  #print(f"Measure: {measure} and parameter: {parameter}")
  return 1 / measure

def process_comparisons(graph, routes, function, parameter=None) -> Dict[Tuple[int, int], int]:
  results = {}
  comparisons = {}
  routes_by_index = []
  for i in range(len(routes)):
      routes_by_index.append(i)
      results[i] = function(graph, routes[i], parameter) if parameter else function(graph, routes[i])
  
  route_pairs = sorted(map(sorted, combinations(set(routes_by_index), 2)))
  for pair in route_pairs:
    print(f"Ayuda1: {results[pair[0]]}")
    print(f"Ayuda2: {results[pair[1]]}")
    result_pair_1 = results[pair[1]] if results[pair[1]] != 0 else 0.000001
    result = results[pair[0]] / result_pair_1 if results[pair[0]] / result_pair_1 != 0 else 0.000001
    comparisons[tuple(pair)] = result

  return comparisons
