from typing import List

class Solution:
  def numUniqueEmails(self, emails: List[str]) -> int:
    for email in emails:
      print(email)

problem = Solution()
print(problem.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(problem.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))