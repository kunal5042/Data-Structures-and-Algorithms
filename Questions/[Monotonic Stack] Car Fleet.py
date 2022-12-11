# Question: https://leetcode.com/problems/car-fleet/
# Medium
from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos, spd) for pos, spd in zip(position, speed)]
        pairs.sort()
        
        stack = []
        for idx in reversed(range(len(pairs))):
            pos, spd = pairs[idx]
            # calculate the time at which this car reaches dest
            dest_time = (target - pos) / spd
            stack.append(dest_time)
            if len(stack) >= 2:
                # if this car's time at which it reaches dest
                # is smaller than the dest time of previous stack top
                # that means, they intersect and become a car fleet
                if stack[~0] <= stack[~1]:
                    stack.pop()
     
        # return car fleets
        return len(stack)
            
            
'''

# Kunal Wadhwa

'''


class Node:
    def __init__(self, label):
        self.label = label
        self.dependencies  = set()
        
    def add_dependency(self, other_node):
        self.dependencies.add(other_node)
        
    def __lt__(self, other_node):
        len(self.dependencies) < other_node.dependencies
        
class CustomGraph:
    def __init__(self, recipes, ingredients, supplies):
        self.nodes = {}
        self.supplies = set()
        self.ingredient_not_available_for_this_recipe = set()
        self.initialize_nodes(recipes, supplies)
        self.build_success = self.build_graph(recipes, ingredients)
        
    def initialize_nodes(self, recipes, supplies):
        for ingredient in supplies:
            self.nodes[ingredient] = Node(ingredient)
            self.supplies.add(self.nodes[ingredient])
        for recipe_name in recipes: self.nodes[recipe_name] = Node(recipe_name)
    
    def build_graph(self, recipes, ingredients) -> bool:
        for recipe_name, ingredients_required in zip(recipes, ingredients):
            for ingredient in ingredients_required:
                if ingredient not in self.nodes:
                    self.ingredient_not_available_for_this_recipe.add(recipe_name)
                else:
                    self.nodes[recipe_name].add_dependency(self.nodes[ingredient])
        return True
    
    def can_make(self, recipe):
        callstack = set()
        visited  = set()
        
        def helper(node) -> bool:
            if node in callstack:
                if node not in self.supplies:
                    return False
            if node in visited  : return True
            
            visited.add(node)
            callstack.add(node)
            
            for dependency in node.dependencies:
                if helper(dependency) is False:
                    return False
            
            callstack.remove(node)
            return True
        
        return helper(self.nodes[recipe])
    
    def get_recipes_we_can_make(self, recipes):
        result  = []
        for recipe in recipes:
            if recipe in self.ingredient_not_available_for_this_recipe: continue
            if self.can_make(recipe) is True:
                result.append(recipe)
        return result
        
             
    
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = CustomGraph(recipes, ingredients, supplies)
        return graph.get_recipes_we_can_make(recipes)
