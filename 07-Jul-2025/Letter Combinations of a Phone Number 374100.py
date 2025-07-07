# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        res = []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(index, path):
            if index == len(digits):
                res.append(path)
                return

            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return res
