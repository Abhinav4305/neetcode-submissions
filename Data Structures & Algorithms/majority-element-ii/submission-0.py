class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        count = 0
        lst = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                count+=1
                if count>n:
                    lst.append(nums[i])
        return list(set(lst))