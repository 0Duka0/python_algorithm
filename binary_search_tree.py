
class Node:
  
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def __str__(self):
    # Node クラスのインスタンスを文字列表現にする
    left = f'[{self.left.value}]' if self.left else '[]'
    right = f'[{self.right.value}]' if self.right else '[]'
    return f'{left} <- {self.value} -> {right}'


class BinarySearchTree:

  def __init__(self):
    self.nodes = []

  def add_node(self, value):
    node = Node(value)
    if self.nodes:
      # 自分の親ノードを探す
      parent, direction = self.find_parent(value)
      if direction == 'left':
        parent.left = node
      else:
        parent.right = node
    # この木のノードとして格納
    self.nodes.append(node)

  def find_parent(self, value):
    node = self.nodes[0]
    # node がNone になるまでループを回す
    while node:
      p = node # 戻り値の候補(親かもしれない)として取っておく
      if p.value == value:
        raise ValueError('すでにある値と同じ値を格納することはできません.')
      if p.value > value:
        direction = 'left'
        node = p.left
      else:
        direction = 'right'
        node = p.right
    return p, direction


btree = BinarySearchTree()
for v in [10, 20, 12, 4, 3, 9, 30]:
  btree.add_node(v)

for node in btree.nodes:
   print(node)

bstree = BinarySearchTree()
for v in sorted([10, 20, 12, 4, 3, 9, 30]):
  bstree.add_node(v)

for node in bstree.nodes:
  print(node)
