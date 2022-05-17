import pytest

from bicycle_graph_builder import *
from cycleway_graph_builder import *
from surface_graph_builder import *
from criteria_comparator import *
from path_processor import *

class TestPathProcessor:
  def setup_method(self, method):
    """ setup any state tied to the execution of the given method in a
    class.  setup_method is invoked for every test method of a class.
    """
   
    self.bicycle_graph = BicycleGraphBuilder().build()
    self.cycleway_graph = CyclewayGraphBuilder().build()
    self.surface_graph = SurfaceGraphBuilder().build()

  def test_cycleway_path(self):
    """Given a known path it should return an appropiate path"""

    criteria_comparator = CriteriaComparator(['cycleway', 'surface'])
    comparisons = {('cycleway', 'surface'): 9}
    criteria_comparator.compare_criteria(comparisons, 'Criteria')

    path_processor = PathProcessor(self.bicycle_graph, self.cycleway_graph, self.surface_graph, criteria_comparator)
    path = path_processor.get_path("Julian Alvarez, 400, Buenos Aires", "Julian Alvarez, 800, Buenos Aires", "length")
    assert len(path) == 9

  def test_cycleway_path_complex(self):
    """Given a known path it should return an appropiate path"""

    criteria_comparator = CriteriaComparator(['cycleway', 'surface'])
    comparisons = {('cycleway', 'surface'): 9}
    criteria_comparator.compare_criteria(comparisons, 'Criteria')

    path_processor = PathProcessor(self.bicycle_graph, self.cycleway_graph, self.surface_graph, criteria_comparator)
    path = path_processor.get_path("Santos Dumont, 3294, Buenos Aires", "Lavalleja, 701 Buenos Aires", "length")
    assert len(path) == 32

  def test_surface_path_complex(self):
    """Given a known path it should return an appropiate path"""

    criteria_comparator = CriteriaComparator(['cycleway', 'surface'])
    comparisons = {('cycleway', 'surface'): 1/9}
    criteria_comparator.compare_criteria(comparisons, 'Criteria')
    
    path_processor = PathProcessor(self.bicycle_graph, self.cycleway_graph, self.surface_graph, criteria_comparator)
    path = path_processor.get_path("Santos Dumont, 3294, Buenos Aires", "Lavalleja, 701 Buenos Aires", "length")
    assert len(path) == 46

  def test_length_path_complex(self):
    """Given a known path it should return an appropiate path"""

    criteria_comparator = CriteriaComparator(['cycleway', 'surface', 'length'])
    comparisons = {('length', 'surface'): 5, ('length', 'cycleway'): 5, ('cycleway', 'surface'): 1}
    criteria_comparator.compare_criteria(comparisons, 'Criteria')
    
    path_processor = PathProcessor(self.bicycle_graph, self.cycleway_graph, self.surface_graph, criteria_comparator)
    path = path_processor.get_path("Lavalleja, 840, Buenos Aires", "Acoyte, 235 Buenos Aires", "length")
    assert len(path) == 41
