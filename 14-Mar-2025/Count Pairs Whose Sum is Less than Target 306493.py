# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        sorted_nums=sorted(nums)
        i,j=0,len(nums)-1
        count =0
        while i <j:
            if sorted_nums[i] +sorted_nums[j] <target:
                count +=(j-i)
                i +=1
            else:
                j -=1
        return count