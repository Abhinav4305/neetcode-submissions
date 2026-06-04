class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lst = []
        m = max(prices)
        for i in range(len(prices)-1):
            if prices[i] > prices[i+1]:
                continue
            else:
                lst.append(prices[i+1] - prices[i])
        

        return sum(lst)


