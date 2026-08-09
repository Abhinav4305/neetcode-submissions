class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        cur_max = nums[0]
        cur_min = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            temp_max = cur_max

            cur_max = max(cur_max * num, num, num * cur_min)
            cur_min = min(temp_max * num, num, num * cur_min)
            global_max = max(global_max, cur_max)
        
        return global_max