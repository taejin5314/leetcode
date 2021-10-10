class Solution:
  def msbPos(self, n):
    msb_p = -1
    while (n > 0):
      n = n >> 1
      msb_p += 1
    
    return msb_p

  def rangeBitwiseAnd(self, left: int, right: int) -> int:
    result = 0

    while (left > 0 and right > 0):
      msb_l = self.msbPos(left)
      msb_r = self.msbPos(right)

      if msb_l != msb_r:
        break

      msb_val = 1 << msb_l
      result += msb_val

      left -= msb_val
      right -= msb_val

    return result

problem = Solution()
print(problem.rangeBitwiseAnd(5, 7))
print(problem.rangeBitwiseAnd(0, 0))
print(problem.rangeBitwiseAnd(1, 2147483647))