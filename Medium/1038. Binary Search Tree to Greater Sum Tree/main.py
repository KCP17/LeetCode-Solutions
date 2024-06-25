# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        '''
        Every node's value should be changed to the sum of ITSELF + EVERYTHING ON ITS RIGHT-HAND SIDE (ONLY a node's right-hand-side nodes have greater values than its value):
            1. All values of its right-subtree nodes
            2. The value of its parent (only if the current node is the left node of its parent, that means its parent is on its right-hand side)
            3. The value of its parent's right subtree (only if the current node is the left node of its parent, just like the above)
        '''
        def dfs(node):
            if not node: # Base case
                return
            dfs(node.right) # Go deep down to the right and sum everything
            self.cur += node.val # We add the sum of everything on the right to the value of itself
            node.val = self.cur # And that'll be our node's new value
            # Everything on the left should be added with current node's value since they're left children of current, and that does work since current node's value was added to `self.cur` and left children can use that
            # We also accumulate those left nodes' values (sum everything on the left) but don't modify current's value anymore as we finished doing that before
            # Those left nodes are on the left-hand side of current so the current node doesn't need to care about them (because they don't affect current's value), but later as we move towards the left there might be nodes that treat the current's left-hand side as their right-hand size, and so they need the sum of these current's left nodes
            dfs(node.left)
        
        self.cur = 0 # Provisional sum as we traverse each node
        dfs(root) # Start searching and modifying the nodes from the root
        return root # Return the whole modified tree
