# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        newList=[int(i) for i in nums]
        newList.sort()
        for i in range(len(newList),-1,-1):
            if k==0:
                return str(newList[i])
            k-=1