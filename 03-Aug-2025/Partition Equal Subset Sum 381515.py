# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        memo = {}

        def dp(i, curr_sum):
            if curr_sum == target:
                return True
            if curr_sum > target or i >= len(nums):
                return False

            key = (i, curr_sum)
            if key not in memo:
                memo[key] = dp(i + 1, curr_sum + nums[i]) or dp(i + 1, curr_sum)
            return memo[key]

        return dp(0, 0)
