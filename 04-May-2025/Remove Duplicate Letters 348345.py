# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last={}
        for i,char in enumerate(s):
            last[char]=i
        stack=[]
        seen=set()

        for i,char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and i < last[stack[-1]]:
                    seen.discard(stack.pop())
                stack.append(char)
                seen.add(char)
        return "".join(stack)


        