# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, add):
            if not node:
                return None
            l = dfs(node.left, True)
            r = dfs(node.right, False)
            if l is None and r is None:
                return node.val if add else 0
            elif l is not None and r is not None:
                return l + r
            else:
                return l if l is not None else r
        return dfs(root, False)
