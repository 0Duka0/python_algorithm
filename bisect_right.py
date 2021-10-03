
def bisect_right(a, x, lo=0, hi=None):
  if lo < 0:
    raise ValueError('lo must be non-negative')
  if hi is None:
    hi = len(a)
  while lo < hi:
    mid = (lo+hi) // 2
    if x < a[mid]: hi = mid
    else: lo = mid + 1
  return lo

import random
random.seed(5)
my_array = [random.randint(0, 100) for i in range(15)]
my_array.sort()
print(bisect_right(my_array, 32))
