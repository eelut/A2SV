# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            i = bisect_left(res, n)
            if i == len(res):
                res.append(n)
            else:
                res[i] = n
        return len(res)
