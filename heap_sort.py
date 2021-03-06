import heapq
import random

def heap_sort(array):
  heap = []
  for v in array:
    heapq.heappush(heap, v)
  return [heapq.heappop(heap) for i in range(len(heap))]

my_array = [random.randint(0, 100) for i in range(15)]
print(my_array)

print(heap_sort(my_array))
