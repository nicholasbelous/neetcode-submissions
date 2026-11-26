# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val == root.val or q.val == root.val:
            return root
        if root == None:
            return None

        def side_checker(r, n):
            if r == None:
                return False
            if r.val == n.val:
                return True

            return side_checker(r.left, n) or side_checker(r.right, n)

        p_left = side_checker(root.left, p)
        p_right = side_checker(root.right, p)
        q_left = side_checker(root.left, q)
        q_right = side_checker(root.right, q)

        if p_left and q_left:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_right and q_right:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


