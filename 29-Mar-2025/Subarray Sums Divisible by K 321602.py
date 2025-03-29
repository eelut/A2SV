# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res=0
        prefix_sum=0
        prefix_count={0:1}

        for n in nums:
            prefix_sum +=n
            rem=prefix_sum %k
            res +=prefix_count.get(rem,0)
            prefix_count[rem]=prefix_count.get(rem,0) +1
        return res


                       