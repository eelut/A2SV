# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n<0:
            return self.myPow(1/x,-n)
        if n == 0: return 1
        if n == 1: return x
        computed = self.myPow(x, n // 2)
        computed *= computed
        if n % 2 == 0: return computed
        else: return x * computed
        