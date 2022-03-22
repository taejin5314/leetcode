class Solution:
  def getSmallestString(self, n: int, k: int) -> str:
    res = []
    while n > 0:
      diff = n * 26 - k
			
      if diff == 0:
        res.extend('z' * n)
        break
      elif diff > 25:
        let = 'a'
        k -= 1
      else:
        code = ord('a') + 26 - diff - 1
        let = chr(code)
        k -= 26 - diff
         
      res.append(let)
      n -= 1
         
    return ''.join(res)