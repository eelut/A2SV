# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        
        
        def dfs(r,c):
            if r >= rows or c >= cols or r < 0 or c < 0:
                return 1 
            if grid[r][c] == 0:
                return 1
            if grid[r][c] == 2:
                return 0
            grid[r][c]=2

            return dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1) 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                   return dfs(r,c)