# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        j=0
        while i <len(s) and j <len(t):
            if s[i]==t[j]:
                i +=1
                j+=1
            else:
                i+=1
        return (len(t)-j)

                