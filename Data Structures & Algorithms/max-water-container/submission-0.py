class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = []
        for i in range(n):
            for j in range(i+1, n):
                res.append(min(heights[i], heights[j])*(j-i))
                j+= 1
        return max(res)