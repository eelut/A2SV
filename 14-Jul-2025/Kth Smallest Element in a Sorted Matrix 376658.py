# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

from bisect import bisect_right

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            mid = (low + high) // 2
            cnt = 0
            for row in matrix:
                cnt += bisect_right(row, mid)
            if cnt < k:
                low = mid + 1
            else:
                high = mid
        return low