# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        values={")":"(","}":"{","]":"["}

        for c in s:
            if c in values:
                if stack and stack[-1]==values[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            
        