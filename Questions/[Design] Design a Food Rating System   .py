# Question: https://leetcode.com/problems/design-a-food-rating-system/
# Medium
from typing import Optional, List

from heapq import heapify, heappop, heappush
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.server = {}
        self.food_to_cuisine = {}
        self.menu = defaultdict(list)
        self.populate_menu(foods, cuisines, ratings)
        
    # O(len(food)) Time and O(len(food)) Space
    def populate_menu(self, foods, cuisines, ratings):
        for idx in range(len(cuisines)):
            self.menu[cuisines[idx]].append((-ratings[idx], foods[idx]))
            self.server[foods[idx]] = ratings[idx]
            self.food_to_cuisine[foods[idx]] = cuisines[idx]
            
        # heapify is O(n), hence more efficient than n times heappush operations which is n*log(n)
        for cuisine in self.menu:
            heapify(self.menu[cuisine])

    # O(log(len(self.menu[self.food_to_cuisine[food]]))) Time
    def changeRating(self, food: str, new_rating: int) -> None:
        # updating / lazy deletion from heap
        self.server[food] = new_rating
        heappush(self.menu[self.food_to_cuisine[food]], ((-new_rating, food)))

    # O(log(self.menu[cuisine])) Time
    def highestRated(self, cuisine: str) -> str:
        while len(self.menu[cuisine]) > 0:
            rating, food = self.menu[cuisine][0]
            if self.server[food] == -rating:
                return food

            # obsolete entry
            heappop(self.menu[cuisine])

'''

# Kunal Wadhwa

'''