# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:

        MOD = 1337

        def mod_pow(x, n):
            res = 1
            x %= MOD
            for _ in range(n):
                res = (res * x) % MOD
            return res
        result = 1
        for digit in b:
            result = mod_pow(result, 10) * mod_pow(a, digit) % MOD
        
        return result
       

    

        