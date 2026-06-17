class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minIndex ,maxIndex = 0,0
        maxProfit = 0
        for i in range(len(prices)):

            if prices[i] < prices[minIndex]:
                minIndex = maxIndex = i
            if prices[i] > prices[maxIndex]:
                maxIndex = i
            maxProfit = max(maxProfit, prices[maxIndex]-prices[minIndex])
        
        return maxProfit

