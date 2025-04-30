# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([(i, t) for i, t in enumerate(tickets)])
        time = 0
        while queue:
            index, count = queue.popleft()
            count -= 1
            time += 1
            if count > 0:
                queue.append((index, count))
            if index == k and count == 0:
                return time


    
    

    
        

        
            
        
        
            
       
                
                
                    
            
            
       
    
        