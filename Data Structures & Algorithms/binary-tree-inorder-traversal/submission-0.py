# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        trav = []

        def orderer(root):
            if root is None:
                return
            
            left = orderer(root.left)
            trav.append(root.val)
            right = orderer(root.right)
        
        orderer(root)

        return trav