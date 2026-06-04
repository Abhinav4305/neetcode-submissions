class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        k = sorted(nums)
        if n%2==0:
            return k[int(n/2)-1]
        else:
            return k[int((n+1)/2)-1]
        
            