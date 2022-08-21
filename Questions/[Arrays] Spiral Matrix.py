# Questions: https://leetcode.com/problems/spiral-matrix/
# Medium
# Traversals can be tricky
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        output = list()
        colstart, colend = 0, len(matrix[0])
        rowstart, rowend = 0, len(matrix)
        toprow  , botrow = 0, len(matrix)-1
        leftcol , rightcol = 0, len(matrix[0])-1
        
        while leftcol <= rightcol and toprow <= botrow:

            for col in range(colstart, colend):
                output.append(matrix[toprow][col])

            toprow += 1
            rowstart += 1
            
            for row in range(rowstart, rowend):
                output.append(matrix[row][rightcol])

            rightcol -= 1
            colend   -= 1
            rowend   -= 1
            

            for col in reversed(range(colstart, colend)):
                output.append(matrix[botrow][col])

            botrow   -= 1
            colstart += 1

            for row in reversed(range(rowstart, rowend)):
                output.append(matrix[row][leftcol])

            leftcol  += 1

        return output[0: len(matrix)*len(matrix[0])]
    
# Kunal Wadhwa
