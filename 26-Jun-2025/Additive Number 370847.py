# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        for i in range(1, n):
            for j in range(i+1, n):
                first = num[:i]
                second = num[i:j]
                
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue
                
                if check(first, second, num[j:]):
                    return True
        return False

def check(first: str, second: str, remaining: str) -> bool:
    while remaining:
        sum_str = str(int(first) + int(second))
        
        if not remaining.startswith(sum_str):
            return False
        
        remaining = remaining[len(sum_str):]
        first, second = second, sum_str
    
    return True