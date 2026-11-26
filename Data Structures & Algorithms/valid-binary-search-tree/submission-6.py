# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def valid(root, n_min, n_max):
            if root is None:
                return True

            if root.val < n_min or root.val > n_max:
                return False

            return valid(root.left, n_min, root.val) and valid(root.right, root.val, n_max)
        
        return valid(root, float("-inf"), float("inf"))
        
        