class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i==k:
                return nums[n - i] 
