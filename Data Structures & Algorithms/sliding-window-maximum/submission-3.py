class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        r = k - 1
        n = len(nums)
        while l <= n - k:
            res.append(max(nums[l: r + 1]))
            l += 1
            r += 1
        return res