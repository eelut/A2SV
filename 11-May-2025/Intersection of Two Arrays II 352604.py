# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c=Counter(nums2)
        res=[]
        for n in nums1:
            if c[n]>0:
                res.append(n)
                c[n]-=1
        return res


        