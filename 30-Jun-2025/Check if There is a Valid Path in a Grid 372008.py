# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: [(0, -1), (0, 1)],     
            2: [(-1, 0), (1, 0)],      
            3: [(0, -1), (1, 0)],      
            4: [(0, 1), (1, 0)],       
            5: [(0, -1), (-1, 0)],     
            6: [(0, 1), (-1, 0)]       
        }

        visited = set([(0, 0)])  
        destination = (len(grid) - 1, len(grid[0]) - 1)

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            if (row, col) == destination:
                return True

            for row_change, col_change in directions[grid[row][col]]:
                new_row = row + row_change
                new_col = col + col_change                
                if (
                    inbound(new_row, new_col)
                    and (new_row, new_col) not in visited
                    and (-row_change, -col_change) in directions[grid[new_row][new_col]]
                ):
                    visited.add((new_row, new_col))
                    if dfs(new_row, new_col):
                        return True

            return False  
        return dfs(0, 0) 

            