class Solution:
  def brokenCalc(self, startValue: int, target: int) -> int:
    if target<=startValue:
      return startValue-target
    else:
      res=0
      while startValue<target:
        if target%2==1:
          target+=1
        else:
          target=target//2
        res+=1
      res+=(startValue-target)
      return res