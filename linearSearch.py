
def linear_search(array, target):
  for v in array:
    if target == v:
      return True
  return False

import random
random.seed(5)
my_array = [random.randint(0, 100) for i in range(15)]

print(linear_search(my_array, 50))
