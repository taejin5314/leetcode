# class Trie:
#   def __init__(self):
#     self.trie = {}

#   def insert(self, word: str) -> None:
#     tmp = self.trie
#     for elm in word:
#       if elm not in tmp:
#         tmp[elm] = {}
#       tmp = tmp[elm]

#     tmp["end"] = True

#   def search(self, word: str) -> bool:
#     tmp = self.trie

#     for elm in word:
#       if elm in tmp:
#         tmp = tmp[elm]
#       else:
#         return False

#     return True if "end" in tmp else False

#   def startsWith(self, prefix: str) -> bool:
#     tmp = self.trie

#     for elm in prefix:
#       if elm in tmp:
#         tmp = tmp[elm]
#       else:
#         return False
    
#     return True
class Node:
  def __init__(self):
    self.next = {}
    self.end = False
    self.count = 0
    
class Trie:
  def __init__(self):
    self.trieNode = Node()

  def insert(self, word: str) -> None:
    node = self.trieNode

    for elm in word:
      if elm not in node.next:
        node.next[elm] = Node()
      node.next[elm].count += 1
      node = node.next[elm]
    
    node.end = True

  def search(self, word: str) -> bool:
    node = self.trieNode

    for elm in word:
      if elm in node.next:
        node = node.next[elm]
      else:
        return False
    
    return node.end
  
  def startsWith(self, prefix: str) -> int:
    node = self.trieNode

    for elm in prefix:
      if elm in node.next:
        node = node.next[elm]
      else:
        return 0

    return node.count
  
  def searchPattern(self, node, target: str) -> int:
    if target == '':
      if node.end:
        return node.count
      return False

    for i, elm in enumerate(target):
      if elm == '.':
        for c in node.next.keys():
          return self.searchPattern(node.next[c], target[i+1:])
      elif elm in node.next:
        node = node.next[elm]
      else:
        return False
    
    return node.count


obj = Trie()
obj.insert("apple")
print(obj.search("app"))
obj.insert("ape")
obj.insert("app")
print(obj.search("pp"))
print(obj.search("apple"))
print(obj.search("ap"))
print(obj.startsWith("ap"))
print(obj.searchPattern(obj.trieNode, "...."))