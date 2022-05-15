import osmnx as ox
from graph import *

PLACE = 'Autonomous City of Buenos Aires, Argentina'
NETWORK_TYPE = 'bike'

class BicycleGraphBuilder(Graph):
  """
  Class that creates a graph that contains each street of the city.
  - nodes: each corner of the city
  - edges: they will exist if it's posible to get from a corner to the other in bike
  """
  def __init__(self):
    self.configure()
    graph = self.__create_graph()
    Graph.__init__(self, graph)

  def __create_graph(self):
      return ox.graph.graph_from_place(PLACE, network_type=NETWORK_TYPE, simplify=False, retain_all=True)
