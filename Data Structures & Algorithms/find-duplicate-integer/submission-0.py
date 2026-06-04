class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lst = []
        for i in range(len(nums)):
            lst.append(nums[i])
            i+=1
            if nums[i] in lst:
                return nums[i]
            continue

        
        