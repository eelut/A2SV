# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.binSearch(nums,target,True)
        right=self.binSearch(nums,target,False)
        return[left,right]

    def binSearch(self,nums,target,left):
        i=-1
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target >nums[m]:
                l=m+1
            elif target<nums[m]:
                r=m-1
            else:
                i=m
                if left:
                    r=m-1
                else:
                    l=m+1
        return i
        


              
        
        