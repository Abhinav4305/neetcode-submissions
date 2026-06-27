# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return (0, 0)
            
            rob_left, skip_right = helper(node.left)
            rob_right, skip_left = helper(node.right)

            rob_loot = node.val + skip_left + skip_right
            skip_loot = max(rob_left, skip_right) + max(rob_right, skip_left)

            return (rob_loot, skip_loot)
        
        final_choices = helper(root)
        return max(final_choices)