# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        i=0
        if len(p) > len(s):
            return []
        p_count=Counter(p)
        for i in range(len(s)-len(p)+1):
            s_count=Counter(s[i:i+len(p)])
            if s_count==p_count:
                ans.append(i)
            
        return ans


        