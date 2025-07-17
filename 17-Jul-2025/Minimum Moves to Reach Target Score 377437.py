# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0
        while target>1:
            if maxDoubles ==0:
                count+=(target-1)
                break
            elif target%2==0:
                maxDoubles-=1
                target=target//2
            else:
                target-=1
            count+=1  
            
        return count
