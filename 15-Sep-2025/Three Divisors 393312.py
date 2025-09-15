# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        root = isqrt(n)
        if root ** 2 != n:
            return False
        if root < 2:
            return False
        for i in range(2, int(root**0.5)+1):
            if root % i == 0:
                return False
        return True