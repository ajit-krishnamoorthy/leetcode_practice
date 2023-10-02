class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for x in prices[1:]:
            if x - minPrice > maxProfit:
                maxProfit = x - minPrice
            if x < minPrice:
                minPrice = x
        return maxProfit