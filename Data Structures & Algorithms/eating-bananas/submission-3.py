class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = r

        while l <= r:
            k = (l + r)//2
            total_time = 0
            for p in piles:
                total_time += math.ceil((p)/k)
            if total_time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

