class Solution:
  def breakPalindrome(self, palindrome: str) -> str:
    palindrome = list(palindrome)
    count = 0
    if len(palindrome) < 2:
      return ''
    else:
      for i, c in enumerate(palindrome):
        if c != 'a':
          palindrome[i] = 'a'
          if len(set(palindrome)) == 1:
            palindrome[i] = c
            palindrome[-1] = 'b'
          return ''.join(palindrome)
        else:
          count += 1
    
    if count == len(palindrome):
      palindrome[-1] = 'b'
      return ''.join(palindrome)

problem = Solution()
print(problem.breakPalindrome("abccba"))
print(problem.breakPalindrome("a"))
print(problem.breakPalindrome("aa"))
print(problem.breakPalindrome("aba"))
