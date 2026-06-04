class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lst=[]
        res = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    res = max(res, prices[j] - prices[i])
                else:
                    None
        return res
