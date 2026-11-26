# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left = root.left
        right = root.right

        if left:
            if left.val >= root.val:
                return False
        if right:
            if right.val <= root.val:
                return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)
            