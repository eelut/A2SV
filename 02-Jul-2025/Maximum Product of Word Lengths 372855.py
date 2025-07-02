# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: list[str]) -> int:
        n = len(words)
        masks = [0] * n
        for i, word in enumerate(words):
            mask = 0
            for c in set(word):
                mask |= 1 << (ord(c) - 97)
            masks[i] = mask
        maxVal = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    maxVal = max(maxVal, len(words[i]) * len(words[j]))
        return maxVal