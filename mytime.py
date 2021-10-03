
import timeit

def my_timeit(text):
  print (timeit.timeit(text, globals = globals(), number=1))
