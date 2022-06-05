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

    def get_paths(self, points):
        first_paths = []
        second_paths = []
        all_markers = []

        for origin, destination in zip(points, points[1:]):
          print(f"Origin: {origin} - destination: {destination}")
          paths, markers = self.__get_paths(origin + ", Buenos Aires", destination + ', Buenos Aires')
          for marker in markers:
            all_markers.append(marker)
          first_paths.append(paths[0])
          second_paths.append(paths[1])

        #print(f"First paths: {first_paths}")
        #print(f"Second paths: {second_paths}")

        first_paths_flatten =  list(dict.fromkeys([item for sublist in first_paths for item in sublist]))
        second_paths_flatten = list(dict.fromkeys([item for sublist in second_paths for item in sublist]))

        #print(f"First paths flatten: {first_paths_flatten}")
        #print(f"Second paths flatten: {second_paths_flatten}")

        return self.__paths_to_html([first_paths_flatten], all_markers)

    def __get_paths(self, origin, destination):
        paths = self.path_processor.get_paths(origin, destination, self.criteria_comparator)
        markers = self.path_processor.get_markers()
        return paths, markers
      
    def __paths_to_html(self, paths, markers):
        paths_html = []
        for path in paths:
          map_plot = ox.plot_route_folium(self.bicycle_graph, path, color="#ff80ab")
          for marker in markers:
            marker.add_to(map_plot)
          paths_html.append(map_plot._repr_html_())
        return paths_html
        