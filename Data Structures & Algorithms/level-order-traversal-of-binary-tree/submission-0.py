# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        levels = [[root]]

        def level_finder(nodes):
            node_lis = []
            for n in nodes:
                if n == None:
                    continue
                if n.left:
                    node_lis.append(n.left)
                if n.right:
                    node_lis.append(n.right)
            return node_lis

        while levels[-1] != []:
            next_lev = level_finder(levels[-1])
            levels.append(next_lev)
        levels.pop()

        for l in levels:
            for v in range(len(l)):
                if l[v] != None:
                    l[v] = l[v].val


        return levels

        

        