class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        count = 0
        for i in range(len(coins)):
            if amount % coins[i] == 0:
                count += 1
        for j in range(len(coins)):
            for k in range(j, len(coins)):
                if coins[j] + coins[k] == amount:
                    count += 1
        return count