import osmnx as ox
from geopy.geocoders import Nominatim
import networkx as nx

class PathProcessor:
  def __init__(self, graph):
    self.graph = graph

  def save_path(self, origin, destination, optimizer, file_name):
    locator = Nominatim(user_agent = "BiciMap")
    origin_location = locator.geocode(origin)
    origin_location_coordinates = (origin_location.latitude, origin_location.longitude)

    dest_location = locator.geocode(destination)
    dest_location_coordinates = (dest_location.latitude, dest_location.longitude)

    origin_node = ox.get_nearest_node(self.graph, origin_location_coordinates)
    dest_node = ox.get_nearest_node(self.graph, dest_location_coordinates)

    shortest_route = nx.shortest_path(self.graph,
                                  origin_node,
                                  dest_node,
                                  weight=optimizer)

    shortest_route_map = ox.plot_route_folium(self.graph, shortest_route)
    shortest_route_map.save(file_name)