# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        a=0
        i=0
        while i <len(chars):
            letter=chars[i]
            count=0
            while i <len(chars) and chars[i]==letter:
                count +=1
                i +=1
            chars[a]=letter
            a +=1
            if count > 1:
                for digits in str(count):
                    chars[a]=digits
                    a +=1
        return a
        