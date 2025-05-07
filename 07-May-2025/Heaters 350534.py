# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0

        for house in houses:
            distance =self.findHeater(house,heaters)
            res=max(res,distance)
        return res
    
    def findHeater(self,house,heaters):
        left,right=0,len(heaters)-1

        while left <=right:
            mid=(left+right)//2
            if heaters[mid]==house:
                return 0
            elif heaters[mid] <house:
                left=mid +1
            else:
                right=mid -1
        dist_left=abs(house-heaters[right]) if right >=0 else float('inf')
        dist_right=abs(house-heaters[left]) if left <len(heaters) else float('inf')                
        return  min(dist_left,dist_right)
        