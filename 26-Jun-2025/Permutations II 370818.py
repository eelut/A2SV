# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        lst=[]
        lr=100
        nums.sort()
        dc={i:False for i in range(0,len(nums))}
        def sub(arr):
            if len(arr)==len(nums):
                lst.append(arr[:])
                return
            for i in range(len(nums)):
                if dc[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not dc[i-1]:
                    continue
                dc[i]=True
                arr.append(nums[i])
                sub(arr)
                arr.pop()
                dc[i]=False
        arr=[]
        sub(arr)
        return lst