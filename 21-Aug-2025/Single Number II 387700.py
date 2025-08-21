# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums):
        count = defaultdict(int)
        
        for x in nums:
            count[x] += 1

        for x, freq in count.items():
            if freq == 1:
                return x
        
        return -1