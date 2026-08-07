class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        while True:
            totaltime = 0
            for pile in piles:
                totaltime += math.ceil(pile/k)
            
            if totaltime <= h:
                return k
            k +=1
        return k