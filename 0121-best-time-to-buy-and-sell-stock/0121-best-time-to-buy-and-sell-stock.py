class Solution(object):
    def maxProfit(self, prices):
        minimum = prices[0]
        maximum = 0
        for i in range(1,len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                profit = prices[i] - minimum
                if profit > maximum:
                    maximum = profit
        return maximum
        