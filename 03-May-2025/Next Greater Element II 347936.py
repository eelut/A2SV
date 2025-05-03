# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums=nums*2
        res=[-1] *n
        stack=[]
        for i in range (len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                idx =stack.pop()
                if idx <n :
                    res[idx]=nums[i]
            if i <n :
                stack.append(i)
        return res
        