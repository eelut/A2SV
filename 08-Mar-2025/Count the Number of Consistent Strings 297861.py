# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set=set(allowed)
        consistent_words=0
        for word in words:
            if all(char in allowed_set for char in word):
                consistent_words +=1
        return consistent_words
       

        