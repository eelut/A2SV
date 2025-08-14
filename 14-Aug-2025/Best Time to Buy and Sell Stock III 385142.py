# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold1 = float('-inf')
        sell1 = 0
        hold2 = float('-inf')
        sell2 = 0

        for p in prices:
            hold1 = max(hold1, -p)
            sell1 = max(sell1, hold1 + p)
            hold2 = max(hold2, sell1 - p)
            sell2 = max(sell2, hold2 + p)

        return sell2
