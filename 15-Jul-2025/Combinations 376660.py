# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
     def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr,first_num):
            if len(curr) == k:
                ans.append(curr[:])
                return
            # pruning
            need=k-len(curr)
            remain=n-first_num + 1
            available=remain-need
            for num in range(first_num, first_num + available +1):
                curr.append(num)
                backtrack(curr,num+1)
                curr.pop()
           
        ans = []
        backtrack([],1)
        return ans
       
           
            
   
            
        
        