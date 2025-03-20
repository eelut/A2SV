# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        sum_nums=0
        min_length=float('inf')
        for right in range(len(nums)):
            sum_nums +=nums[right]
            while sum_nums >= target:
                min_length=min(min_length,(right-left +1))
                sum_nums -=nums[left]
                left+=1
            
        return 0 if min_length==float('inf') else min_length
            
