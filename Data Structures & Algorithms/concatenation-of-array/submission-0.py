class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans.extend(nums)
        for num in nums:
            ans.append(num)
        return ans
