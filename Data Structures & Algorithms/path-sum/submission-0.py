# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(r, s):
            if r.left == None and r.right == None:
                if (s + r.val) == targetSum:
                    return True
                else:
                    return False
            elif r.left == None:
                return dfs(r.right, s + r.val)
            elif r.right == None:
                return dfs(r.left, s + r.val)
            
            return dfs(r.left, s + r.val) or dfs(r.right, s + r.val)

        return dfs(root, 0)