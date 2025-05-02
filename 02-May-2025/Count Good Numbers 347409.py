# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

MOD=10**9+7
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even=(n+1)//2
        odd=n//2
        return (pow(5,even,MOD)*pow(4,odd,MOD)) %MOD
        