class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            for i in range(1, len(nums)):
                if (num+1) in nums:
                    count += 1
                    num += 1
                    
                
            else:
                return count+1