import osmnx as ox

class GraphBuilder:
  """
  Class that creates a graph that contains each street of the city.
  - nodes: each corner of the city
  - edges: they will exist if it's posible to get a path with the given criteria
  """
  def __init__(self, graph):
    G = ox.add_edge_speeds(graph)
    self.graph = ox.add_edge_travel_times(G)
    self.__fix_two_way_cycleways()
    #self.plot()

  def configure(self):
    useful_tags = ox.settings.useful_tags_way + ['cycleway', 'bicycle', 'oneway:bicycle', 'surface']
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

  def build(self): return self.graph

  def print(self):  
    for u,v,k,d in self.graph.edges(keys=True, data=True): print(f"u: {u} - v: {v} - k: {k} - d: {d}")
