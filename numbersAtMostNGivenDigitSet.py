from typing import List

class Solution:
  def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
    digits = list(map(int, digits))

    def countNumsWithPrefix(prefix=0):
      if prefix > n:
        return 0
      return sum(countNumsWithPrefix(prefix * 10 + d) for d in digits) + 1

    return countNumsWithPrefix() - 1


problem = Solution()
print(problem.atMostNGivenDigitSet(['1','3','5','7'], 100))