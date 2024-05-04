## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/35a07e1c-8c2f-417c-9ecb-0e77c0ef1bab)

## Code (Python3)
```python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if p.val != q.val: # If cur values are not equal -> False
                return False
            
            if not p.left and not p.right and not q.left and not q.right: # If cur nodes of both trees have no children -> True cuz we've already checked that their values are equal
                return True

            if p.left and q.left: # If left children of cur nodes of both trees exist
                res_left = dfs(p.left, q.left) # Search on the left of both trees
                if not res_left: # If the left is not identical then no need to search on the right anymore
                    return False
            elif (not p.left and q.left) or (not q.left and p.left): # If cur node of this tree has left child but the other doesn't -> False
                return False
            
            if p.right and q.right: # Same as searching on the left
                res_right = dfs(p.right, q.right)
                if not res_right:
                    return False
            elif (not p.right and q.right) or (not q.right and p.right):
                return False

            return True # both `res_left` & `res_right` must be true for the program to come down this far so just return True 

        if not p and not q: return True # If both are empty
        if (p and not q) or (q and not p) : return False # One is empty but the other has values
        return dfs(p, q)
```
## Time & Space:
* Time: $$O(N)$$
* Space: $$O(H)$$ with H is the height of tree, but O(N) worst case
