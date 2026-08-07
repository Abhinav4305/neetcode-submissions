class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort(reverse = True)
        for i in range(n):
            if i==k:
                return nums[i-1] 
