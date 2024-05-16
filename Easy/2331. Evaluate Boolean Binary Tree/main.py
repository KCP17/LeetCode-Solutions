# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool: # DFS
        if not root.left: # If a node doesn't have children (full binary tree so doesn't have a left child also means doesn't have a right child) -> leaf node
            return root.val # 0 indicates False, 1 indicates True
        if root.val == 2: # Non-leaf node, value == 2 --> Bitwise OR on left & right children
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        if root.val == 3: # Non-leaf node, value == 3 --> Bitwise AND on left & right children
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
