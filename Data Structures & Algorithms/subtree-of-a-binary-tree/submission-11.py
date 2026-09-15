# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        def isSameTree(root, subRoot):
            if root is None and subRoot is None:
                return True
            elif root is None and subRoot is not None:
                return False
            elif subRoot is None and root is not None:
                return False
            else:
                if root.val == subRoot.val:
                    return isSameTree(root.left, subRoot.left) and  isSameTree(root.right, subRoot.right)
                else:
                    return False

        if root is None:
            return False
        elif root.val == subRoot.val:
            return isSameTree(root, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
