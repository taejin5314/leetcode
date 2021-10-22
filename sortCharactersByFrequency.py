class Solution:
  def frequencySort(self, s: str) -> str:
    hashMap = {}

    for c in s:
      if c in hashMap:
        hashMap[c] += 1
      else:
        hashMap[c] = 1
    
    hashMap = {k: v for k, v in sorted(hashMap.items(), key=lambda item: item[1], reverse=True)}

    result = ''
    for c in hashMap:
      for _ in range(hashMap[c]):
        result += c

    return result

problem = Solution()
print(problem.frequencySort("tree"))
print(problem.frequencySort("cccaaa"))
print(problem.frequencySort("Aabb"))