# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans=[-1] *len(nums)
        left,total=0,0
        size=2*k +1
        for right in range (len(nums)):
            total+=nums[right]
            if right-left+1==size:
                ans[left+k]=(total//size)
                total -=nums[left]
                left +=1
        return ans



        