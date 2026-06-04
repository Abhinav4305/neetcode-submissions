class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)//3
        nums.sort()
        i = 0

        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j +=1
            if (j-i) > n:
                res.append(nums[i])
            i = j
        return res