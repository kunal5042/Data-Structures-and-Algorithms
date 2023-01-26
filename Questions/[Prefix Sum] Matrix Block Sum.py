# Question: https://leetcode.com/problems/matrix-block-sum/
# Medium
from typing import Optional, List

class Solution:
    # brute-force: correct answer but time limit exceeded
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        
        def get_sum(idx, jdx):
            result = 0
            visited = set()
            queue = deque([(idx, jdx)])
            directions = [
                (1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)
            ]
            
            while len(queue) != 0:
                row, col = queue.popleft()
                if (row, col) in visited: continue
                visited.add((row, col))
                
                result += mat[row][col]
                
                for x, y in directions:
                    adj_row = row + x
                    adj_col = col + y
                    
                    if (adj_row, adj_col) not in visited and \
                    adj_row >= idx - k and adj_row <= idx + k and \
                    adj_col >= jdx - k and adj_col <= jdx + k and \
                    adj_row >= 0 and adj_row < ROWS and \
                    adj_col >= 0 and adj_col < COLS:
                        queue.append((adj_row, adj_col))
            return result
        
        answer = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for row in range(ROWS):
            for col in range(COLS):
                answer[row][col] = get_sum(row, col)
        
        return answer
    
    # prefix-sum
    # O(R*C) time and O(R*C) space
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        sums = [[mat[r][c] for c in range(COLS)] for r in range(ROWS)]
        
        for row in range(ROWS):
            for col in range(1, COLS):
                sums[row][col] += sums[row][col-1]
        
        for row in range(1, ROWS):
            for col in range(COLS):
                sums[row][col] += sums[row-1][col]
                
        sums.insert(0, [0 for _ in range(COLS)])
        for row in range(ROWS+1):
            sums[row].insert(0, 0)
                
        for row in range(ROWS):
            for col in range(COLS):
                r1, c1 = max(0, row-k), max(0, col-k)
                r2, c2 = min(ROWS-1, row+k), min(COLS-1, col+k)
                
                r1, r2, c1, c2 = r1+1, r2+1, c1+1, c2+1
                
                mat[row][col] = sums[r2][c2]
                mat[row][col] -= (sums[r2][c1-1] + sums[r1-1][c2])
                mat[row][col] += sums[r1-1][c1-1]
        
        return mat


# January 26, 2023

'''

# Kunal Wadhwa

'''