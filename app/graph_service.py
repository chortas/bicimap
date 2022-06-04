import json

from cycleway_graph_builder import *
from surface_graph_builder import *
from bicycle_graph_builder import *
from path_processor import *
from criteria_comparator import *

class GraphService(object):
    def __init__(self):
      self.bicycle_graph = BicycleGraphBuilder().build()
      cycleway_graph = CyclewayGraphBuilder().build()
      surface_graph = SurfaceGraphBuilder().build()
      self.path_processor = PathProcessor(self.bicycle_graph, cycleway_graph, surface_graph)
      self.criteria_comparator = CriteriaComparator()

    def save_comparisons(self, body):
      comparisons = {}
      for elemen in body:
        comparisons[tuple(elemen.split(','))] = body[elemen]
      return self.criteria_comparator.compare_criteria(comparisons, 'Criteria')

    def get_path(self, origin, destination):
        path = self.path_processor.get_path(origin, destination, self.criteria_comparator)
        shortest_route_map = ox.plot_route_folium(self.bicycle_graph, path)
        shortest_route_map.save("cycleway.html")
        
