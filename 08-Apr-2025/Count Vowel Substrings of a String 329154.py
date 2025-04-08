# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels=set("aeiou")
        total =0
        n =len(word)

        for i in range(n):
            if word[i] not in vowels:
                continue
            seen ={}
            for j in range(i,n):
                if word[j] not in vowels:
                    break
                seen [word[j]]=1
                if len(seen)==5:
                    total +=1
        return total
        