import osmnx as ox
from graph_builder import *

PLACE = 'Autonomous City of Buenos Aires, Argentina'
NETWORK_TYPE = 'bike'
SURFACE_CUSTOM_FILTER = '["surface"~"asphalt|concrete|paved"]'

class SurfaceGraphBuilder(GraphBuilder):
  """
  Class that creates a graph that contains each street of the city.
  - nodes: each corner of the city
  - edges: they will exist if it's posible to get from a corner to the other in bike and it is pavimented
  """
  def __init__(self):
    self.configure()
    graph = self.__create_graph()
    self.__remove_streets_without_speed(graph)
    GraphBuilder.__init__(self, graph)

  def __create_graph(self):
      return ox.graph.graph_from_place(PLACE, network_type=NETWORK_TYPE, simplify=False, custom_filter=SURFACE_CUSTOM_FILTER,
    retain_all=True)

  def __remove_streets_without_speed(self, graph):
    edges_to_remove = []

    for u,v,k,d in graph.edges(keys=True, data=True):
      if 'speed_kph' not in d and 'maxspeed' not in d:
        edges_to_remove.append((u, v, k, d))

    graph.remove_edges_from(edges_to_remove)