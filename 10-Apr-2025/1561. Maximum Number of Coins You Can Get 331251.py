# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res=0
        l,r=0,len(piles)-1
        while l <r:
            r -=1
            res +=piles[r]
            r-=1
            l +=1
        return res