# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k==0:
            return
        size=len(nums)
        k=k if k <=size else k %size
        nums[k:] ,nums[:k]=nums[:size-k],nums[size -k:]
        