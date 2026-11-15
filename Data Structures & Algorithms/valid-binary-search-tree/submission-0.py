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

        root_binary = None

        if root.left == None and root.right == None:
            root_binary = True
        elif root.right == None and root.val >= root.left.val:
            root_binary = True
        elif root.left == None and root.val <= root.right.val:
            root_binary = True
        elif root.val <= root.right.val and root.val >= root.left.val:
            root_binary = True
        else:
            root_binary = False

        return root_binary and self.isValidBST(root.left) and self.isValidBST(root.right)
        
        