class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lst=[]
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    lst.append(prices[j]-prices[i])
                else:
                    lst.append(0)
        if len(lst) > 1:
            return max(lst)
        else:
            return 0
