class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = []
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums) - 1):
            res.append(nums[i] * nums[i+1])
        
        if max(res) > max(nums):
            return max(res)
        else:
            return max(nums)