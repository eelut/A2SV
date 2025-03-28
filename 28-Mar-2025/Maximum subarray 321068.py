# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        total=0
        for n in nums:
            # to start fresh
            if total <0:
                total=0
            total +=n
            res=max(res,total)
        return res
        