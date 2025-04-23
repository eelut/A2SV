# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counted_s=Counter(s)
        for i in range(len(s)):
            if counted_s[s[i]]==1:
                return i
        return -1

        