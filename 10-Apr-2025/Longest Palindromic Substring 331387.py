# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index={}
        max_length=0
        start=0
        for end in range (len(s)):
            if s[end] in char_index:
                start =max(start,char_index[s[end]]+1)
            char_index[s[end]]=end
            max_length=max(max_length,end-start+1)
        return max_length

        