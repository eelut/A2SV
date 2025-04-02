# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        squareroot=set()
        for i in range (int(sqrt(c)) +1):
            squareroot.add(i *i)
        
        a=0
        while a*a <=c:
            target =c - a*a
            if target in squareroot:
                return True
            a +=1
        return False
        