from typing import List

class StreamChecker:

  def __init__(self, words: List[str]):
    self.s = ''
    self.dict = collections.defaultdict(set)
    for w in words:
      self.dict[w[-1]].add(w)

  def query(self, letter: str) -> bool:
    self.s += letter
    return any(self.s.endswith(w) for w in self.dict[letter])
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)