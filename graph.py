import osmnx as ox
from geopy.geocoders import Nominatim
import networkx as nx

PLACE = 'Autonomous City of Buenos Aires, Argentina'
NETWORK_TYPE = 'bike'
CUSTOM_FILTER = '["bicycle"]'

class Graph:
  """
  Class that represents the graph that contains each street of the city.
  - nodes:  each corner of the city
  - edges: they will exist if it's posible to get from a corner to the other in bike
  """
  def __init__(self):
    self.__configure()
    self.graph = ox.graph.graph_from_place(PLACE, network_type='bike', simplify=False, custom_filter=CUSTOM_FILTER, retain_all=True)
    self.__fix_two_way_cycleways()

  def __configure(self):
    useful_tags = ox.settings.useful_tags_way + ['cycleway'] + ['bicycle'] + ["oneway:bicycle"]
    ox.utils.config(use_cache=True, log_console=True, useful_tags_way=useful_tags)

  def __fix_two_way_cycleways(self):
    edges_to_add = []
    for u,v,k,d in self.graph.edges(keys=True, data=True):
      if d.get('bicycle')=='designated' and d.get('oneway:bicycle')=='no':
        d['oneway'] = False
        edges_to_add.append((v, u, k, d))
    self.graph.add_edges_from(edges_to_add)

  def plot(self):
    return ox.plot.plot_graph(self.graph, bgcolor='#c0c2c2', node_color='#f0ede6', node_size=5, edge_color='#0cc7b4', edge_linewidth=1,save=True)

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
