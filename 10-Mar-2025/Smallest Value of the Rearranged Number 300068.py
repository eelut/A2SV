# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        nums=sorted(str(abs(num)), reverse =num <0)
        if nums[0] == '0':
            non_zero = next((i for i, n in enumerate(nums) if n != '0'), 0)
            nums[0] , nums[non_zero]=nums[non_zero] , nums[0]
        return int("".join(nums)) *(1 if num >=0 else -1)
        


        
            
  



        