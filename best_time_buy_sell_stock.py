class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        size = len(prices)
        result = 0
        maxRight = [prices[size - 1]] * size
        maxRightNum = prices[size - 1]
        for i in range (1, size):
            if prices[size - i] > maxRightNum:
                maxRightNum = prices[size - i]
            maxRight[size - 1 - i] = maxRightNum

        for i in range (size - 1):
            profit = maxRight[i] - prices[i]
            if profit > result: result = profit
        
        return result

solulu = Solution()
prices=[5,1,5,6,7,1]
print (solulu.maxProfit(prices))