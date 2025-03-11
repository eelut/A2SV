# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        #for better lookup
        num_set=set(nums)
        max_length=0

        for num in num_set:
            length=0
            current_num=num
            while current_num in num_set:
                length +=1
                current_num=current_num **2
            
            if length >1:
                max_length=max(max_length,length)

        return max_length if max_length>1 else -1
