import ahpy

# For now we will only compare cycleways against not pavimented paths.
# TODO: add comparison with time and length criteria
IA = {2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
class CriteriaComparator:
  def __init__(self):
    self.alternatives = []

  def compare_criteria(self, comparisons, name, n_comparisons):
    self.criteria = self.__compare(comparisons, name, n_comparisons)

  def compare_alternative(self, comparisons, name, n_comparisons):
    self.alternatives.append(self.__compare(comparisons, name, n_comparisons))

  def get_best_route(self):
    self.criteria.add_children(self.alternatives)
    results = self.criteria.target_weights
    return max(results, key=(lambda key: results[key]))

  def __compare(self, comparisons, name, n_comparisons):
    results = ahpy.Compare(name=name, comparisons=comparisons, precision=3, random_index='saaty')
    if (not self.__is_consistent(results, n_comparisons)):
      raise Exception("Data provided is not consistent")
    return results

  def __is_consistent(self, results, n_comparisons):
    print(f"Target weights: {results.target_weights}")
    print(f"Consistency ratio: {results.consistency_ratio}")
    return results.consistency_ratio <= IA[n_comparisons]
    
