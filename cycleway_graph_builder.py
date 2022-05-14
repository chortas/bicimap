import osmnx as ox
import networkx as nx

PLACE = 'Autonomous City of Buenos Aires, Argentina'
NETWORK_TYPE = 'bike'
BICYCLE_CUSTOM_FILTER = '["bicycle"="designated"]'
HIGHWAY_CUSTOM_FILTER = '["highway"="cycleway"]'

class CyclewayGraphBuilder:
  """
  Class that creates a graph that contains each street of the city.
  - nodes: each corner of the city
  - edges: they will exist if it's posible to get from a corner to the other in bike
  """
  def __init__(self):
    self.__configure()
    bicycle_graph = ox.graph.graph_from_place(PLACE, network_type='bike', simplify=False, custom_filter=BICYCLE_CUSTOM_FILTER, 
    retain_all=True)
    highway_graph = ox.graph.graph_from_place(PLACE, network_type='bike', simplify=False, custom_filter=HIGHWAY_CUSTOM_FILTER, 
    retain_all=True)
    self.graph = nx.compose(bicycle_graph, highway_graph)
    self.__fix_two_way_cycleways()
    self.plot()

  def __configure(self):
    useful_tags = ox.settings.useful_tags_way + ['cycleway', 'bicycle', 'oneway:bicycle', 'surface']
    ox.utils.config(use_cache=True, log_console=True, useful_tags_way=useful_tags)

  def __fix_two_way_cycleways(self):
    edges_to_add = []
    edges_to_remove = []

    surfaces = set()

    for u,v,k,d in self.graph.edges(keys=True, data=True):
      if d.get('bicycle')=='designated' and d.get('oneway:bicycle')=='no':
        d['oneway'] = False
        edges_to_add.append((v, u, k, d))
      
      if 'surface' in d and d['surface'] not in ('asphalt', 'concrete', 'paved'): 
        edges_to_remove.append((u, v, k, d))

    self.graph.add_edges_from(edges_to_add)
    self.graph.remove_edges_from(edges_to_remove)
    

  def plot(self):
    return ox.plot.plot_graph(self.graph, bgcolor='#c0c2c2', node_color='#f0ede6', node_size=5, edge_color='#0cc7b4', edge_linewidth=1,save=True)

  def build(self): return self.graph