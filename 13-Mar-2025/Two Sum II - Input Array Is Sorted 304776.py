# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0, len(numbers) -1
        ans=[]
        while left < right:
            sum_of_two=numbers[left]+numbers[right]
            if sum_of_two < target:
                left +=1
            elif sum_of_two > target:
                right -=1
            else:
                return [left+1,right+1]


        