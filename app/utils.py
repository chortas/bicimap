from itertools import islice, combinations
from geopy.geocoders import Nominatim
import osmnx as ox
import networkx as nx

def k_shortest_paths(G, source, target, k, weight=None):
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

def calculate_measurable_comparison(graph, route):
  length = 0
  for u, v in zip(route, route[1:]):
    length += graph.get_edge_data(u, v)[0]['length']
  return length

def process_comparisons(graph, routes, function):
  results = {}
  comparisons = {}
  routes_by_index = []
  for i in range(len(routes)):
      routes_by_index.append(i)
      results[i] = function(graph, routes[i])
  
  route_pairs = sorted(map(sorted, combinations(set(routes_by_index), 2)))
  for pair in route_pairs:
    comparisons[tuple(pair)] = 1 / (results[pair[1]] / results[pair[0]])

  #print(f"Pairs: {route_pairs}")
  #print(f"Comparisons: {comparisons}")

  return comparisons
