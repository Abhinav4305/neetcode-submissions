class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = []
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums) - 1):
            res.append(nums[i] * nums[i+1])
        return max(res) if max(res) > max(nums) else max(res)