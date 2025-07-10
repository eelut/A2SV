# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        
        def bfs(q):
            count = 0
            while q:
                i, j, curr_c = q.popleft()
                count = curr_c if curr_c > count else count
                if (0 <= i < m ) and (0 <= j < n ) and grid[i][j] in (1, 2):
                    if (i, j) not in visited:
                        visited.add((i, j))
                        q.append((i, j+1, curr_c+1))
                        q.append((i+1, j, curr_c+1))
                        q.append((i, j-1, curr_c+1))
                        q.append((i-1, j, curr_c+1))
            return count-1
        
        res = 0
        q = deque()
        no_fresh_orange = True
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    no_fresh_orange = False
                elif grid[r][c] == 2:
                    q.append((r, c, 0))  
        res = bfs(q)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited: 
                    return -1  
        return 0 if no_fresh_orange else res