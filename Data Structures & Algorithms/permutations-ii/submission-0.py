class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        visited = set()

        def backtrack():
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in visited:
                    continue
                visited.add(i)
                path.append(nums[i])
                backtrack()
                visited.remove(i)
                path.pop()
        backtrack()
        return res