class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums) - 1):
            res.append(nums[i] * nums[i+1])
        return max(res)