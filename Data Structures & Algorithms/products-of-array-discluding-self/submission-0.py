class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        for i in range(len(nums)):
            pdt = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                pdt *= nums[j]
            res[i] = pdt
        return res
        