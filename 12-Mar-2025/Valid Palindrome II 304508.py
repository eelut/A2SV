# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left , right=0,len(s)-1
        while left <= right:
            if s[left] !=s[right]:
                option1=s[:left] +s[left+1:]
                option2=s[:right] +s[right+1:]
                return option1==option1[::-1] or option2==option2[::-1]
            left +=1
            right -=1
        return True

        

        