# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(index, target, path):
            if target == 0:
                res.append(path[:])
                return

            if target < 0:
                return

            for i in range(index, len(candidates)):
                num = candidates[i]
                path.append(num)                         # choose
                backtrack(i, target - num, path)         # explore (reuse allowed)
                path.pop()                               # un-choose (backtrack)

        backtrack(0, target, [])
        return res
