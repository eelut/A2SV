# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans=1
        left=0
        count=0
        n=len(s)

        for right in range (1,n):
            if s[right] ==s[right -1]:
                count +=1
            while count >1:
                if s[left] ==s[left +1]:
                    count -=1
                left +=1
            ans =max (ans,right-left+1)
        return ans  