class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentBest=prices[0]
        maxProfit=0
        for price in prices:
            if price<currentBest:
                currentBest=price
            profit=price-currentBest
            maxProfit=max(maxProfit,profit)
        return maxProfit