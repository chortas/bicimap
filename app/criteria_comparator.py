import ahpy

IA = {2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}

class CriteriaComparator:
  def __init__(self, comparison_criteria):
    self.comparison_criteria = comparison_criteria

  def compare_criteria(self, comparisons, name):
    self.criteria = self.__compare(comparisons, name, len(self.comparison_criteria))

  def compare_alternative(self, comparisons, name, n_comparisons):
    return self.__compare(comparisons, name, n_comparisons)

  def is_criteria(self, criteria):
    return criteria in self.comparison_criteria

  def get_best_route(self, alternatives):
    self.criteria.add_children(alternatives)
    results = self.criteria.target_weights
    return max(results, key=(lambda key: results[key]))
    # return max(results.values())

  def get_max_IC(self):
    return max(IA.keys())

  def get_optimizer(self):
    travel_time_weigth = self.criteria.target_weights.get('travel_time', 0)
    length_weigth = self.criteria.target_weights.get('length', 0)
    return 'travel_time' if travel_time_weigth > length_weigth else 'length' 

  def __compare(self, comparisons, name, n_comparisons):
    results = ahpy.Compare(name=name, comparisons=comparisons, precision=3, random_index='saaty') 
    if (not self.__is_consistent(results, n_comparisons)):
      raise Exception("Data provided is not consistent")
    return results

  def __is_consistent(self, results, n_comparisons):
    return results.consistency_ratio <= IA[n_comparisons]
    
