## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/047bac2c-e9df-43c5-80a7-cf24e9973af5)

## Code (Python3)
```python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right): return 0
        def dfs(node, tmp, res):
            tmp += 1
            if node.left:
                res = max(res, dfs(node.left, tmp, res))
            if node.right:
                res = max(res, dfs(node.right, tmp, res))
            if not node.left and not node.right:
                return max(res, tmp)
            tmp -= 1
            return res

        def root_dfs(root, output):
            if root.left:
                output = max(output, root_dfs(root.left, output))
            if root.right:
                output = max(output, root_dfs(root.right, output))
            if not root.left and not root.right:
                return 1
            
            left_side = dfs(root.left, 0, 0) if root.left else 0
            right_side = dfs(root.right, 0, 0) if root.right else 0
            return max(output, left_side + right_side)
        
        return root_dfs(root, 0)
```
## Note:
2D DFS (My solution):
- Time: $$O(N^2)$$
- Space: $$O(H)$$, worst case $$O(N)$$
