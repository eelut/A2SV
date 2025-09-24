# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = set([1])
        heap = [1]

        for _ in range(n):
            curr = heapq.heappop(heap)  # smallest ugly number
            for i in [2, 3, 5]:
                new_val = curr * i
                if new_val not in seen:
                    seen.add(new_val)
                    heapq.heappush(heap, new_val)

        return curr

