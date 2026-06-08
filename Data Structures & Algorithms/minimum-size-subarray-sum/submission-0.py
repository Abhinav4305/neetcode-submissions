class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        res = float("inf")
        for i in range(len(nums)):
            sum = sum + nums[i]
            while sum >= target:
                res = min(i-left+1, res)
                sum -= nums[left]
                left += 1
        return 0 if res == float("inf") else res
            
