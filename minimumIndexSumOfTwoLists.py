from typing import List

class Solution:
  def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    print(list1, list2)
    return 0

problem = Solution()
print(problem.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
print(problem.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]))
print(problem.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]))
print(problem.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KNN","KFC","Burger King","Tapioca Express","Shogun"]))
print(problem.findRestaurant(["KFC"], ["KFC"]))