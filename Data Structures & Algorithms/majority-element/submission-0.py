class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        k = sorted(nums)
        if n%2==0:
            return k[(n/2)]
        else:
            return k[int((n+1)/2)]
        
            