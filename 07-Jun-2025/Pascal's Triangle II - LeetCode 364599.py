# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        row = [1]

        for _ in range(rowIndex):
            row = [left + right for left, right in zip([0]+row, row+[0])]
            
        return row    