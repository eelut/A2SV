# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        def helper(processed, up):
            if not up:
                return [processed]
            button = int(up[0])
            ans = []
            if 2 <= button <= 6:
                for i in range((button-2)*3, (button-1)*3):
                    ch = chr(ord('a') + i)
                    ans += helper(processed + ch, up[1:])
            elif button == 7:
                for i in range(15, 19):
                    ch = chr(ord('a') + i)
                    ans += helper(processed + ch, up[1:])
            elif button == 8:
                for i in range(19, 22):
                    ch = chr(ord('a') + i)
                    ans += helper(processed + ch, up[1:])
            elif button == 9:
                for i in range(22, 26):
                    ch = chr(ord('a') + i)
                    ans += helper(processed + ch, up[1:])
            return ans

        return helper("", digits)
        
    
    
        