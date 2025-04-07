# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        shift_ans =[0] *(n+1)
        for shift in shifts:
            start,end,direction =shift
            shift_ans[start] +=(1 if direction ==1 else -1)
            if end +1<n:
                shift_ans[end+1] -=(1 if direction ==1 else -1)
        currentShift =0
        shiftList=list(s)
        for i in range(n):
            currentShift +=shift_ans[i]
            netShift=(currentShift %26 +26)%26
            shiftList[i] = chr((ord(shiftList[i]) - ord('a') + netShift) % 26 + ord('a'))
            
        return "".join(shiftList)
        



        