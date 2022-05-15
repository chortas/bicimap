import osmnx as ox
from geopy.geocoders import Nominatim
import networkx as nx
from itertools import islice

'''
Auxiliary functions. TODO: move to utils folder
'''

def k_shortest_paths(G, source, target, k, weight=None):
  return list(islice(nx.shortest_simple_paths(G, source, target, weight=weight), k))

def get_coordinates(location):
  locator = Nominatim(user_agent = "BiciMap")
  location_geocoded = locator.geocode(location)
  return (location_geocoded.latitude, location_geocoded.longitude)

class PathProcessor:

  def save_path(self, origin, destination, optimizer, file_name, graph, full_graph):
    origin_location_coordinates = get_coordinates(origin)
    dest_location_coordinates = get_coordinates(destination)

    origin_node = ox.get_nearest_node(graph, origin_location_coordinates)
    dest_node = ox.get_nearest_node(graph, dest_location_coordinates)

    shortest_routes = []

    try:
      shortest_route = nx.shortest_path(graph, origin_node, dest_node, weight=optimizer)
      shortest_routes.append(shortest_route)
    except:
      graph_aux = nx.DiGraph(full_graph)
      shortest_routes = k_shortest_paths(graph_aux,
                                  origin_node,
                                  dest_node,
                                  10,
                                  weight=optimizer)
    finally:
      for i in range(len(shortest_routes)):
        route = shortest_routes[i]
        shortest_route_map = ox.plot_route_folium(full_graph, route)
        shortest_route_map.save(str(i) + file_name)
