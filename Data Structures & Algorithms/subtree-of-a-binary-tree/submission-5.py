# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if((root == None and subRoot != None) or (root != None and subRoot == None)):
            return False
        if(root == None and subRoot == None):
            return True

        left = root.left
        right = root.right 

        subLeft = subRoot.left
        subRight = subRoot.right
        
        return (
            (root.val == subRoot.val and self.isSubtree(left, subLeft) and self.isSubtree(right, subRight))
            or self.isSubtree(left, subRoot) or self.isSubtree(right, subRoot)
        )


        