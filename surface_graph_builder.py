import osmnx as ox
from graph import *

PLACE = 'Autonomous City of Buenos Aires, Argentina'
NETWORK_TYPE = 'bike'
SURFACE_CUSTOM_FILTER = '["surface"~"asphalt|concrete|paved"]'

class SurfaceGraphBuilder(Graph):
  """
  Class that creates a graph that contains each street of the city.
  - nodes: each corner of the city
  - edges: they will exist if it's posible to get from a corner to the other in bike and it is pavimented
  """
  def __init__(self):
    self.configure()
    graph = self.__create_graph()
    Graph.__init__(self, graph)

  def __create_graph(self):
      return ox.graph.graph_from_place(PLACE, network_type=NETWORK_TYPE, simplify=False, custom_filter=SURFACE_CUSTOM_FILTER, 
    retain_all=True)
