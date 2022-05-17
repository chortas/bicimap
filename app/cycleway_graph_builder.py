import osmnx as ox
from graph_builder import *
import networkx as nx

PLACE = 'Autonomous City of Buenos Aires, Argentina'
NETWORK_TYPE = 'bike'
BICYCLE_CUSTOM_FILTER = '["bicycle"~"designated"]'
HIGHWAY_CUSTOM_FILTER = '["highway"~"cycleway"]'

class CyclewayGraphBuilder(GraphBuilder):
  """
  Class that creates a graph that contains each street of the city.
  - nodes: each corner of the city
  - edges: they will exist if it's posible to get from a corner to the other in bike and via cycleway
  """
  def __init__(self):
    self.configure()
    graph = self.__create_graph()
    GraphBuilder.__init__(self, graph)

  def __create_graph(self):
    bicycle_graph = ox.graph.graph_from_place(PLACE, network_type=NETWORK_TYPE, simplify=False, custom_filter=BICYCLE_CUSTOM_FILTER, 
    retain_all=True)
    highway_graph = ox.graph.graph_from_place(PLACE, network_type=NETWORK_TYPE, simplify=False, custom_filter=HIGHWAY_CUSTOM_FILTER, 
    retain_all=True)
    return nx.compose(bicycle_graph, highway_graph)
