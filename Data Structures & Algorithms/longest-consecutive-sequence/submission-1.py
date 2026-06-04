class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        for num in nums:
            count, curr = 0, num
            while curr in store:
                count += 1
                curr += 1
            res = max(res, count)
        return res