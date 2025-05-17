# 121. Best Time to Buy and Sell Stock
#
# You are given an array `prices` where `prices[i]` is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different
# day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
#
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: No transactions are done. Max profit = 0.
#
# Constraints:
# - 1 <= prices.length <= 10^5
# - 0 <= prices[i] <= 10^4

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')  # Track the minimum price so far
        maxProfit = 0  # Track the maximum profit found
        N = len(prices)

        for i in range(N):
            # Update minPrice if current price is lower
            if prices[i] < minPrice:
                minPrice = prices[i]
            
            # Update maxProfit if current profit is higher
            maxProfit = max(maxProfit, prices[i] - minPrice)

        return maxProfit
