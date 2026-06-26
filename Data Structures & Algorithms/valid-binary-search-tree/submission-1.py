# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.previous_val = float('-inf')
        res = []
        def inorder(node):
            if not node:
                return True
            
            """
            if not inorder(node.left):
               return False
            
            if node.val <= self.previous_val:
                return False
            
            self.previous_val = node.val

            return inorder(node.right)
        return inorder(root)
        """
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
            
        inorder(root)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False                
        return True
        
         