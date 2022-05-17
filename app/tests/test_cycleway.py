import pytest

from bicycle_graph_builder import *
from cycleway_graph_builder import *
from surface_graph_builder import *
from criteria_comparator import *
from path_processor import *

class TestCycleway:
  def setup_method(self, method):
    """ setup any state tied to the execution of the given method in a
    class.  setup_method is invoked for every test method of a class.
    """
    self.bicycle_graph = BicycleGraphBuilder().build()
    self.cycleway_graph = CyclewayGraphBuilder().build()
    self.surface_graph = SurfaceGraphBuilder().build()
    self.criteria_comparator = CriteriaComparator()

  def test_cycleway_path(self):
    """Given a known path it should return an appropiate path"""

    comparisons = {('cycleway', 'surface'): 9}
    self.criteria_comparator.compare_criteria(comparisons, 'Criteria', 2)
    path_processor = PathProcessor(self.bicycle_graph, self.cycleway_graph, self.surface_graph, self.criteria_comparator)
    path = path_processor.get_path("Julian Alvarez, 400, Buenos Aires", "Julian Alvarez, 800, Buenos Aires", "length")
    assert len(path) == 9