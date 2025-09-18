# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        first = second = -1  

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count == 1:
                    first = i
                elif count == 2:
                    second = i
                else:
                    return False  

        return count == 0 or (count == 2 and s1[first] == s2[second] and s1[second] == s2[first])
