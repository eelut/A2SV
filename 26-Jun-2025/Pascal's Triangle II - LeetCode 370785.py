# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        row = [1]

        for i in range(rowIndex):
            next_row=[0]*(len(row) +1)
            for j in range(len(row)):
                next_row[j] +=row[j]
                next_row[j+1] +=row[j]
            row=next_row 
        return row    