class Trie:
  def __init__(self):
    self.trie = {}

  def insert(self, word: str) -> None:
    tmp = self.trie
    for elm in word:
      if elm not in tmp:
        tmp[elm] = {}
      tmp = tmp[elm]

    tmp["end"] = True

  def search(self, word: str) -> bool:
    tmp = self.trie

    for elm in word:
      if elm in tmp:
        tmp = tmp[elm]
      else:
        return False

    return True if "end" in tmp else False

  def startsWith(self, prefix: str) -> bool:
    tmp = self.trie

    for elm in prefix:
      if elm in tmp:
        tmp = tmp[elm]
      else:
        return False
    
    return True
    
obj = Trie()
obj.insert("apple")
print(obj.search("app"))
print(obj.search("apple"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))
print(obj.trie)
