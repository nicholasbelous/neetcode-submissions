# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        root_pointer = root
        
        que = deque([root])
        def invert(root):
            if root is None:
                return
            
            #swap
            root.left, root.right = root.right, root.left

            return [root.left, root.right]

        while que:
            roots = invert(que.popleft())

            for val in roots:
                if val is None:
                    continue
                que.append(val)
        
        return root_pointer