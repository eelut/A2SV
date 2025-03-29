# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution(object):
    def subarraySum(self, nums, k):
        res=0
        curSum=0
        prefixSums={0:1}

        for n in nums:
            curSum +=n
            diff=curSum-k

            res +=prefixSums.get(diff,0)
            prefixSums[curSum]=1 +prefixSums.get(curSum,0)
        return res  