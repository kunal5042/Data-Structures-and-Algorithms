# Question: https://leetcode.com/problems/word-ladder-ii/
# Hard

from copy import copy
from string import ascii_lowercase
from collections import defaultdict, deque
from typing import List

class Solution:
    #
    # time-limit-exceeded
    #
    # depth first search along with backtracking
    # the problem in this solutions is that, we are finding every possible path
    # from begin_word to end_word, whereas we only need the shortest path
    #
    def findLadders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        mutations = defaultdict(list)
        word_list.append(begin_word)

        for word in word_list:
            for idx in range(len(word)):
                mutations[word[:idx] + '*' + word[idx+1:]].append(word)
                
        visited = set()
        paths = []
        def depth_first_search(word, path):
            if word in visited: return
            visited.add(word)
            path.append(word)
            
            if word == end_word:
                paths.append(path.copy())
                path.pop()
                visited.remove(word)
                return
            
            for idx in range(len(word)):
                mutant_template = word[:idx] + '*' + word[idx+1:]
                for mutant in mutations[mutant_template]:
                    if mutant not in visited:
                        depth_first_search(mutant, path)
                        
            visited.remove(word)
            path.pop()
            return
        
        depth_first_search(begin_word, [])
        if len(paths) == 0: return []
        paths.sort(key=len)
        
        shortest_path = len(paths[0])
        end = 1
        for idx in range(1, len(paths)):
            if len(paths[idx]) > shortest_path:
                break
            end += 1
            
        return paths[:end]
    
    # 
    # time-limit-exceeded
    #
    # the optimization here is that, due to the nature of the breadth first search
    # the path we find the first will be the shortest
    #
    # once, we find that path, we can stop looking for paths which have length
    # longer than the shortest path
    #
    # additionally we are removing the already used mutants from the availalbe possible mutations to further optimize
    #
    def findLadders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        mutations = defaultdict(set)

        for word in word_list:
            for idx in range(len(word)):
                mutations[word[:idx] + '*' + word[idx+1:]].add(word)
              
        visited = set()
        paths = []
        queue = deque([[begin_word]])
        mutants_used = set()
        shortest_path_found = False
        
        while len(queue) != 0:   
            if shortest_path_found is True: break
            breadth = len(queue)
            local_visited = set()
            
            for _ in range(breadth):
                path = queue.popleft()
                word = path[~0]

                if word in visited: continue
                local_visited.add(word)
                
                if word == end_word:
                    paths.append(copy(path))
                    shortest_path_found = True
                    continue
                
                for idx in range(len(word)):
                    mutant_template = word[:idx] + '*' + word[idx+1:]
                    for mutant in mutations[mutant_template]:
                        if mutant not in visited and mutant != word:
                            path.append(mutant)
                            queue.append(copy(path))
                            path.pop()
                            mutants_used.add(mutant)
                            
            visited = visited.union(local_visited)
            while len(mutants_used) != 0:
                to_remove = mutants_used.pop()
                for template, available_mutations in mutations.items():
                    if to_remove in available_mutations:
                        available_mutations.remove(to_remove)
                                                
        return paths if len(paths) != 0 else []
                
    def findLadders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        mutations = set(word_list)
        if end_word not in mutations: return []
        
        visited = set()
        paths = []
        
        queue = deque([[begin_word]])
        shortest_path_found = False
        
        while len(queue) != 0:   
            if shortest_path_found is True: break
            breadth = len(queue)
            local_visited = set()
            
            for _ in range(breadth):
                path = queue.popleft()
                word = path[~0]

                if word in visited: continue
                local_visited.add(word)
                
                for idx in range(len(word)):
                    for char in ascii_lowercase:
                        if char == word[idx]: continue
                        mutant = word[:idx] + char + word[idx+1:]
                        if mutant in mutations and mutant not in visited:
                            if mutant == end_word:
                                paths.append(path + [mutant])
                                shortest_path_found = True
                                continue
                            queue.append(path + [mutant])
                            
            visited |= local_visited
            mutations -= local_visited
                                                
        return paths if len(paths) != 0 else []
    
    def findLadders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        possible_mutations = defaultdict(list)
        for word in word_list:
            for idx in range(len(word)):
                possible_mutations[word[:idx]+"*"+word[idx+1:]].append(word)

        if end_word not in word_list:
            return []

        visited1 = defaultdict(list)
        queue1 = deque([begin_word])
        visited1[begin_word] = []

        visited2 = defaultdict(list)
        queue2 = deque([end_word])
        visited2[end_word] = []

        output = []
        def dfs(word, visited, path, paths):
            path.append(word)
            if not visited[word]:
                if visited is visited1:
                    paths.append(path[::-1])
                else:
                    paths.append(path[:])
            for u in visited[word]:
                dfs(u, visited, path, paths)
            path.pop()

        def bfs(queue, visited1, visited2, is_from_begin):
            level_visited = defaultdict(list)
            for _ in range(len(queue)):
                word = queue.popleft()

                for idx in range(len(word)):
                    for mutant in possible_mutations[word[:idx]+"*"+word[idx+1:]]:
                        if mutant in visited2:
                            paths1 = []
                            paths2 = []
                            dfs(word, visited1, [], paths1)
                            dfs(mutant, visited2, [], paths2)
                            if not is_from_begin:
                                paths1, paths2 = paths2, paths1
                            for inter_from_begin in paths1:
                                for inter_from_end in paths2:
                                    output.append(inter_from_begin + inter_from_end)
                        elif mutant not in visited1:
                            if mutant not in level_visited:
                                queue.append(mutant)
                            level_visited[mutant].append(word)
            visited1.update(level_visited)

        while queue1 and queue2 and not output:
            if len(queue1) <= len(queue2):
                bfs(queue1, visited1, visited2, True)
            else:
                bfs(queue2, visited2, visited1, False)

        return output

# April 30, 2023

'''

# Kunal Wadhwa

'''