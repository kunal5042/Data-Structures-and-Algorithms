# Question: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
# Medium
from typing import Optional, List

class Node:
    def __init__(self, label: 'str') -> 'Node':
        self.name = label
        self.dependencies  = set()
        
    def add_dependency(self, other_node: 'Node'):
        self.dependencies.add(other_node)
        
    def __lt__(self, other_node: 'Node'):
        len(self.dependencies) < other_node.dependencies
        
class CustomGraph:
    def __init__(self, recipes: 'List[str]', ingredients: 'List[List[str]]', supplies: 'List[str]') -> 'CustomGraph':
        self.nodes = {}
        self.cannot_make_these_because_of_unkown_ingredient = set()
        self.initialize_nodes(recipes, supplies)
        self.build_graph(recipes, ingredients)
        
    def initialize_nodes(self, recipes, supplies):
        for ingredient in supplies:
            self.nodes[ingredient] = Node(ingredient)
        for recipe_name in recipes: self.nodes[recipe_name] = Node(recipe_name)
    
    def build_graph(self, recipes: 'List[str]', ingredients: 'List[List[str]]'):
        for recipe_name, ingredients_required in zip(recipes, ingredients):
            for ingredient in ingredients_required:
                if ingredient not in self.nodes:
                    self.cannot_make_these_because_of_unkown_ingredient.add(recipe_name)
                    break
                self.nodes[recipe_name].add_dependency(self.nodes[ingredient])
                    
    def can_make(self, recipe: 'str') -> 'bool':
        """Returns true if dependencies for making this recipe can be met successfully"""
        callstack = set()
        visited  = set()
        
        def helper(node) -> bool:
            if node in callstack: return False
            if node in visited  : return True
            
            visited.add(node)
            callstack.add(node)
            
            for dependency in node.dependencies:
                if dependency.name in self.cannot_make_these_because_of_unkown_ingredient:
                    return False
                if helper(dependency) is False:
                    return False
            
            callstack.remove(node)
            return True
        
        return helper(self.nodes[recipe])
    
    def get_recipes_we_can_make(self, recipes: 'List[str]') -> 'List[str]':
        """Returns a list of recipes we can successfully make"""
        result  = []
        for recipe in recipes:
            if recipe in self.cannot_make_these_because_of_unkown_ingredient:
                continue
            if self.can_make(recipe) is True:
                result.append(recipe)
        return result
        
    
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = CustomGraph(recipes, ingredients, supplies)
        return graph.get_recipes_we_can_make(recipes)
'''

# Kunal Wadhwa

'''