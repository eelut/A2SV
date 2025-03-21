# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        ans=0
        current_sum=0
        count={}
        for r in range (len(nums)):
            while count.get(nums[r],0) >0:
                count[nums[l]] -=1
                current_sum -= nums[l]
                l +=1
                
            count[nums[r]]=count.get(nums[r],0) +1
            current_sum +=nums[r]
            ans=max(ans,current_sum)
        return ans
            
            

       
        