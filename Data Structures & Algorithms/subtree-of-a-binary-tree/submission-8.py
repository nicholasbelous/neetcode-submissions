# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root == None and subRoot != None):
            return False
        if(root != None and subRoot == None):
            return False
        if(root == None and subRoot == None):
            return True

        def isMatch(r, s):
            if r == None and s == None: return True
            if r == None or s == None: return False
            return r.val == s.val and isMatch(r.left, s.left) and isMatch(r.right, s.right)

        left = root.left
        right = root.right

        if isMatch(root, subRoot):
            return True



        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        