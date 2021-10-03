
def merge_arrays(left, right=[]):
  res = []
  i, j = 0, 0
  n, m = len(left), len(right)
  # どちらかの配列を調べ尽くしたらそこで終了
  while i < n and j < m:
    if left[i] < right[j]:
      res.append(left[i])
      i += 1
    else:
      res.append(right[j])
      j += 1
  # 残りはそのまま後ろに連結する
  return res + left[i:] + right[j:]

def step(array):
  res = []
  for i in range(0, len(array), 2):
#    print(*array[i:i + 2])
    # 長さ2もしくは1の配列がスライスの結果を返る
    res.append(merge_arrays(*array[i:i+2]))
  return res

def merge_sort(array):
  # すべての数をリストに変換する
  res = [[v] for v in array]
  while len(res[0]) != len(array):
    res = step(res)
  # リストの中にリストが入ってしまうのでこれを取り出す
  return res[0]

def merge_sort_recursion(array):
  if len(array) <= 1:
    return array
  mid_idx = len(array) // 2
  left = array[:mid_idx]
  right = array[mid_idx:]
  return merge_arrays(merge_sort_recursion(left), merge_sort_recursion(right))

import random
random.seed(4)
my_array = [random.randint(0, 100) for i in range(15)]
#print(merge_sort(my_array))
print(merge_sort_recursion(my_array))
