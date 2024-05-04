# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:        
        def recurse(node, leaves):
            if not node.left and not node.right:
                leaves.append(node.val)
                return leaves
            if node.left: recurse(node.left, leaves)
            if node.right: recurse(node.right, leaves)
            return leaves
        
        leaves_1 = recurse(root1, [])
        leaves_2 = recurse(root2, [])
        
        return True if leaves_1 == leaves_2 else False
