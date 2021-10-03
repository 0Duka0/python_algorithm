
def quick_sort(array):
  # 空の配列はそのまま返す
  if array == []:
    return array
  # 最後の要素をpivotにする
  p = random.choice(array)
  left = []
  right = []
  pivots = []
  # pivot との関係で要素を分割する
  for v in array:
    if v < p:
      left.append(v)
    elif v == p:
      pivots.append(v)
    else :
      right.append(v)
  # 左と右は再び関数を適用して返す
  return quick_sort(left) + pivots + quick_sort(right)

import random
random.seed(4)
my_array = [random.randint(0, 100) for i in range(15)]
print(quick_sort(my_array))
