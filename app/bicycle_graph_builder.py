import osmnx as ox
import os
from graph_builder import *

PLACE = 'Autonomous City of Buenos Aires, Argentina'
NETWORK_TYPE = 'bike'

class BicycleGraphBuilder(GraphBuilder):
  """
  Class that creates a graph that contains each street of the city.
  - nodes: each corner of the city
  - edges: they will exist if it's posible to get from a corner to the other in bike
  """
  def __init__(self):
    self.configure()
    graph = self.__load_graph()
    GraphBuilder.__init__(self, graph)

  def __load_graph(self):
      heroku = 'HEROKU' in os.environ
      graph = self.__create_graph() if heroku else ox.load_graphml('bycycle_graph.graphml')
      return graph

  def __create_graph(self):
    graph = ox.graph.graph_from_place(PLACE, network_type=NETWORK_TYPE, simplify=False, retain_all=True)
    #ox.save_graphml(graph, 'bycycle_graph.graphml')
    return graph
