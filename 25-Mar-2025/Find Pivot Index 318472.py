# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0
        total_sum=sum(nums)
        for j in range (len(nums)):
            right_sum=total_sum -(left_sum +nums[j])
            if right_sum == left_sum:
                return j
            left_sum +=nums[j]
        return -1
        