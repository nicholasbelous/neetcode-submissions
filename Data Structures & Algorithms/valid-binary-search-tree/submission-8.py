# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, low, high):
            if root is None:
                return True
            
            left = root.left
            right = root.right

            if left:
                if left.val >= root.val or left.val <= low:
                    return False
            if right:
                if right.val <= root.val or right.val >= high:
                    return False

            return helper(root.left, low, root.val) and helper(root.right, root.val, high)

        return helper(root, float('-inf'), float('inf'))
            