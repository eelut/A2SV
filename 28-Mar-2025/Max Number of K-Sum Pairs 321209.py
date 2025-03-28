# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

from collections import Counter

class Solution:
    def maxOperations(self, nums, k):
        count_map = Counter(nums)  
        operations = 0

        for num in list(count_map.keys()):  
            complement = k - num
            if complement in count_map:  
                if num == complement:
                    operations += count_map[num] // 2
                else:
                    operations += min(count_map[num], count_map[complement])

                del count_map[num]
                if complement in count_map:
                    del count_map[complement]

        return operations
