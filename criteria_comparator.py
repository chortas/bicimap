import ahpy

# For now we will only compare cycleways against not pavimented paths.
# TODO: add comparison with time and length criteria
IA = {2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
class CriteriaComparator:
  def __init__(self, comparisons, n_comparisons): # I assume that I'll get the data from the frontend and I'll create the criteria accordingly in another class
    self.criteria = ahpy.Compare(name='BiciMap', comparisons=comparisons, precision=3, random_index='saaty')
    self.n_comparisons = n_comparisons

  def is_consistent(self):
    print(f"Consistency ratio: {self.criteria.consistency_ratio}")
    return self.criteria.consistency_ratio <= IA[self.n_comparisons]
