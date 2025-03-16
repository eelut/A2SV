# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0 :
            return
        length_1=len(nums1)
        end_index_nums1=length_1 - 1
        while n >0 and m >0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[end_index_nums1]=nums2[n-1]
                n -= 1
            else:
                nums1[end_index_nums1]=nums1[m-1]
                m -= 1
            end_index_nums1 -= 1
        while n >0:
            nums1[end_index_nums1]=nums2[n-1]
            n -= 1
            end_index_nums1 -=1


       
        