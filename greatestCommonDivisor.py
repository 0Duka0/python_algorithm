
import math
import printf
# python標準関数 最大公約数 
print(math.gcd(18915, 14938))

# 自作関数 (簡単な実装方法)
def simple_gcd(a, b):
  if a < b:
    a, b = b, a
  x = b
  while True:
    if a % x == 0 and b % x == 0:
      return x
    x -= 1

#print(simple_gcd(18915, 14938))

# ユークリッドの互除法
# 入力：2つの自然数 a,b
# 出力：最大公約数
# 手続き：
# 1. aをbで割った余りをrとする
# 2. rが0ならば、bを出力すて終了
# 3. aにbを、bにrを代入して手続き1へ戻る
def euclidean_algorithm(a, b):
  while True:
    r = a % b
    if r == 0:
      return b
    a, b = b, r

#print(euclidean_algorithm(18915, 14938))

# 再帰を使った実装
def euclidean_recursion(a, b):
  r = a % b
  if r == 0:
    return b
  return euclidean_recursion(b, r)

print (euclidean_recursion(18915, 14938))
