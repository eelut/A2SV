# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s))==len(set(t))==len(set(zip(s,t)))
