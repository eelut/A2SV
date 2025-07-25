# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []

        m, n = len(mat), len(mat[0])
        diagonals = {}

        for r in range(m):
            for c in range(n):
                key = r + c
                if key not in diagonals:
                    diagonals[key] = []
                diagonals[key].append(mat[r][c])

        result = []

        for k in range(m + n - 1):
            if k % 2 == 0:
                result.extend(reversed(diagonals[k]))
            else:
                result.extend(diagonals[k])

        return result
