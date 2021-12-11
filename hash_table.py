## 作る機能
## 1. キーと値のペアを保存
## 2. キーを指定することで値を取得
## 3. 1つのハッシュテーブルの同一のキーには、複数の値を格納できない
## 4. 違うキーのハッシュ値が同じになることはある(ハッシュの衝突)

class HashTable:

  def __init__(self, table_size=100):
    # ターブルのサイズを引数で変更できるようにしている
    self.data = [[] for i in range(table_size)]
    self.n = table_size


  # オブジェクトのハッシュ値を計算し返す
  def get_hash(self, v):
    return hash(v) % self.n 

  def search(self, key):
    # key を使って値を探す
    i = self.get_hash(key)
    for j, v in enumerate(self.data[i]):
      if v[0] == key:
        return (i, j)
    return (i, -1)

  def set(self, key, value):
    # データを格納するべき場所を探す
    i, j = self.search(key)
    if j != -1:
      self.data[i][j][1] = value
    else:
      # 新たなデータとして付け加える
      self.data[i].append([key, value])

  def get(self, key):
    i, j = self.search(key)
    if j != -1:
      return self.data[i][j][1]
    # キーが見つかれない場合はエラーを返す
    raise KeyError(f'{key} was not found in this HashTable!')


my_hash_table = HashTable()
my_hash_table.set('taro', 10)
print(my_hash_table.get('taro'))
