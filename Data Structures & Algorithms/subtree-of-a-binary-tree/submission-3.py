# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root == None and subRoot == None):
            return True
        if(root == None or subRoot == None):
            return False
        
        # recursive call checking that all of one roote subtree is in subRoot
        if(root.val == subRoot.val 
        and self.isSubtree(root.left, subRoot.left)
        and self.isSubtree(root.right, subRoot.right)
        ):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)