from typing import List

class Solution:
  def maxLength(self, arr: List[str]) -> int:
    maximum = 0
    combinations = ['']
    for i in range(len(arr)):
      for j in range(len(combinations)):
        if len(set(arr[i] + combinations[j])) == len(arr[i] + combinations[j]):
          combinations.append(arr[i] + combinations[j])
          maximum = max(len(arr[i] + combinations[j]), maximum)
    return maximum

problem = Solution()
print(problem.maxLength(["un","iq","ue"]))
print(problem.maxLength(["cha","r","act","ers"]))
print(problem.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
print(problem.maxLength(["a", "abc", "d", "de", "def"]))
print(problem.maxLength(["yy","bkhwmpbiisbldzknpm"]))
print(problem.maxLength(["ogud","ejipchfydrgl","b","kjxmzhnuoisgqvawel","mizlcgdqebwuotfnk","bjvkrgeozidytquchlw","tzjqwumkirxeal","x","rkpuabmo","mxndpcqzua"]))
print(problem.maxLength(["ab","cd","cde","cdef","efg","fgh","abxyz"]))