# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # If our helper doesn't return -1, the tree is balanced
        return self.getHeight(root) != -1

    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Base case: empty node has height 0
        
        # 1. Get heights of subtrees
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        
        # 2. Check for "Emergency Brake" signals from below
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
            
        # 3. If perfectly balanced, return actual height
        return 1 + max(left, right)