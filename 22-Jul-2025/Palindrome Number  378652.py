# Problem: Palindrome Number  - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x %10==0 and x !=0):
            return False
        reversed_int=int(str(x)[::-1])
        if x == reversed_int:
            return True
        else:
            return False


        