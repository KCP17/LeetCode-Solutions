## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/afcba8c5-bd21-4c10-8120-37b313fc911d)

## Code (Python3)
```python3 []
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
```
## Note:
DFS (My solution):
- Time: $$O(N)$$ with N nodes of tree
- Space: $$O(H)$$ on average with H height of tree, but worst case O(N)
