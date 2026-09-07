# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = deque([root])

        while stack:
            node = stack.pop()

            if node == None:
                continue

            output.append(node.val)

            if(node.right):
                stack.append(node.right)
            if(node.left):
                stack.append(node.left)
        
        return output 
