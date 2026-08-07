class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i==k:
                return nums[i+1] 
