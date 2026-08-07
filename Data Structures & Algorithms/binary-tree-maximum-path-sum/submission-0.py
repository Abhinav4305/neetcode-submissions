# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = float(-'inf')

        def solve(node):
            if not node:
                return 0
            left_sum = solve(node.left)
            right_sum = solve(node.right)

            if left_sum < 0:
                left_sum = 0
            if right_sum < 0:
                right_sum = 0
            
            maximum = max(maximum, left_sum + node.val + right_sum)
        return node.val + max(left_sum, right_sum)