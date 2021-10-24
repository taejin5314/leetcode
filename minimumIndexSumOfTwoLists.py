from typing import List

class Solution:
  def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    map = {}
    index = float('inf')
    res = []

    for i, restaurant in enumerate(list1):
      map[restaurant] = i

    for i, restaurant in enumerate(list2):
      if restaurant in map:
        if i + map[restaurant] < index:
          index = i + map[restaurant]
          res = [restaurant]
        elif i + map[restaurant] == index:
          res.append(restaurant)

    return res

problem = Solution()
print(problem.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
print(problem.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]))
print(problem.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]))
print(problem.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KNN","KFC","Burger King","Tapioca Express","Shogun"]))
print(problem.findRestaurant(["KFC"], ["KFC"]))