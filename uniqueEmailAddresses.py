from typing import List

class Solution:
  def numUniqueEmails(self, emails: List[str]) -> int:
    map_local, map_domain = {}, {}
    count = 0
    for email in emails:
      local = ''.join(email.split('@')[0].split('+')[0].split('.'))
      domain = email.split('@')[1]

      if local not in map_local.keys() or domain not in map_domain.keys():
        count += 1

        if local not in map_local.keys():
          map_local[local] = 1
        else:
          map_local[local] += 1
        if domain not in map_domain.keys():
          map_domain[domain] = 1
        else:
          map_domain[domain] += 1
    return count

problem = Solution()
print(problem.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(problem.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))