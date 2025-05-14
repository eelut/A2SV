# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

class Solution:
    def decToBinary(self, n):
        # code here
        if n==0:
            return 0
        else:
            return (n%2 + 10 * self.decToBinary(n//2))
            # return n%2, end=''

