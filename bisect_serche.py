
import bisect
import random
random.seed(5)
my_array = [random.randint(0, 100) for i in range(15)]
my_array.sort()
print(bisect.bisect(my_array, 40))
print(bisect.bisect_right(my_array, 32))
print(bisect.bisect_left(my_array, 32))

