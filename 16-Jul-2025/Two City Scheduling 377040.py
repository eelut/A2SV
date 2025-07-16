# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs=[]
        for a,b in costs:
            diffs.append([b-a ,a,b]) 
        diffs.sort()
        res=0
        for i in range(len(costs)):
            if i<len(costs)//2:
                res+=diffs[i][2]
            else:
                res+=diffs[i][1]
        return res