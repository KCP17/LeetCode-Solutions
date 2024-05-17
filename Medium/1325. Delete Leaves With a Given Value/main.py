# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]: # DFS
        def dfs(node):
            if node.left and dfs(node.left): # Go search for the left child, if that child returns `True` means we have to delete it (look at the logic below)
                node.left = None # Set the left child to `None` to delete it
            if node.right and dfs(node.right): # Go search for the right child, if that child returns `True` means we have to delete it (look at the logic below)
                node.right = None # Set the right child to `None` to delete it

            if not node.left and not node.right and node.val == target: # Reached the leaf (doesn't have both left & right children) and its value == target
                return True # Return `True` to tell its parent to delete it

        dummy = TreeNode(val=0, left=root) # Dummy node to resolve cases where the root is deleted (E.g test case root=[1,1,1], target=1)
        dfs(dummy)
        return dummy.left
