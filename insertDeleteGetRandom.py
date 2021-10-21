import random

class RandomizedSet:

  def __init__(self):
    self.data = []
    self.data_map = {}

  def insert(self, val: int) -> bool:
    if val in self.data_map:
      return False
    
    self.data_map[val] = len(self.data)

    self.data.append(val)
    
    return True

  def remove(self, val: int) -> bool:
    if val not in self.data_map:
      return False

    index = self.data_map[val]
    self.data_map[self.data[-1]] = index
    self.data[index], self.data[-1] = self.data[-1], self.data[index]
    self.data.pop()
    self.data_map.pop(val)

    return True    
    

  def getRandom(self) -> int:
    return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.insert(2)
param_3 = obj.remove(1)
param_4 = obj.getRandom()
print(param_1, param_2, param_3, param_4)