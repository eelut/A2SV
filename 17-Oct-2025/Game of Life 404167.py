# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n, m = len(board), len(board[0])
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(n):
            for j in range(m):
                live_neighbors = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    
                    if 0 <= ni < n and 0 <= nj < m:
                        if board[ni][nj] in [1, 2]:
                            live_neighbors += 1

                if board[i][j] == 1: 
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2 
                else: 
                    if live_neighbors == 3:
                        board[i][j] = 3 
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    board[i][j] = 0 
                elif board[i][j] == 3:
                    board[i][j] = 1 