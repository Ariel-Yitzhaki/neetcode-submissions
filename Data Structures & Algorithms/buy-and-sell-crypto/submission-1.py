class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, temp = 0, prices[0]

        for i in range(1, len(prices)):
            if prices[i] < temp:
                temp = prices[i]
            else:
                res = max(res, prices[i] - temp)
        return res