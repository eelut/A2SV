# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
 # self. remembered and accessible anywhere inside the class — even across different methods.
        self.ans = float('inf')
        
        dist = [0] * k

        def backtrack(i):
            if i == len(cookies):
                self.ans = min(self.ans, max(dist)) 
                return

            for j in range(k):  
                dist[j] += cookies[i]  

                if max(dist) < self.ans:
                    backtrack(i + 1)

                dist[j] -= cookies[i]  

                if dist[j] == 0:
                    break

        backtrack(0)  
        return self.ans
