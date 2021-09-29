class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    s1Map = {}
    for elm in s1:
      if elm in s1Map:
        s1Map[elm] += 1
      else:
        s1Map[elm] = 1
    target = len(s1)

    for i in range(len(s2) - target + 1):
      s2Map = {}
      for j in range(i, i + target):
        if s2[j] in s2Map:
          s2Map[s2[j]] += 1
        else:
          s2Map[s2[j]] = 1

      if s2Map == s1Map:
        return True
    return False

problem = Solution()
print(problem.checkInclusion('ab', 'eidbaooo'))
print(problem.checkInclusion('ab', 'eidboaoo'))
print(problem.checkInclusion('abb', 'eidbaooo'))
print(problem.checkInclusion('abb', 'eidbaooo'))
print(problem.checkInclusion('abcdxabcde', 'abcdeabcdx'))