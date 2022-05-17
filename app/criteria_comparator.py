import ahpy

IA = {2: 0.0, 3: 0.4914, 4: 0.8286, 5: 1.0591, 6: 1.1797, 7: 1.2519, 8: 1.3171, 9: 1.3733, 10: 1.4055, 11: 1.4213, 12: 1.4497,
13: 1.4643, 14: 1.4822, 15: 1.4969, 16: 1.5078, 17: 1.5153, 18: 1.5262, 19: 1.5313, 20: 1.5371, 25: 1.5619, 30: 1.5772,
40: 1.5976, 50: 1.6102, 60: 1.6178, 70: 1.6237, 80: 1.6277, 90: 1.6213, 100: 1.6339}
class CriteriaComparator:
  def __init__(self, comparison_criteria):
    self.alternatives = []
    self.comparison_criteria = comparison_criteria

  def compare_criteria(self, comparisons, name):
    self.criteria = self.__compare(comparisons, name, len(self.comparison_criteria))

  def compare_alternative(self, comparisons, name, n_comparisons):
    self.alternatives.append(self.__compare(comparisons, name, n_comparisons))

  def is_criteria(self, criteria):
    return criteria in self.comparison_criteria

  def get_best_route(self):
    self.criteria.add_children(self.alternatives)
    results = self.criteria.target_weights
    return max(results, key=(lambda key: results[key]))

  def __compare(self, comparisons, name, n_comparisons):
    results = ahpy.Compare(name=name, comparisons=comparisons, precision=3, random_index='dd')
    if (not self.__is_consistent(results, n_comparisons)):
      raise Exception("Data provided is not consistent")
    return results

  def __is_consistent(self, results, n_comparisons):
    #print(f"Target weights: {results.target_weights}")
    #print(f"Consistency ratio: {results.consistency_ratio}")
    return results.consistency_ratio <= IA[n_comparisons]
    
