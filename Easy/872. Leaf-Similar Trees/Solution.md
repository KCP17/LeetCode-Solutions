## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/2b80ea46-bc62-43a8-acf7-53d943db950b)

## Code (Python3)
```python3 []
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
```
## Note:
DFS - Recursion (My solution):
- Time: $$O(N+M+L)$$ with M nodes of tree1, N nodes of tree2, L leaves of each tree
- Space: $$O(N+M+L)$$ worst case due to recursive stack calls, but O(L + height(N) + height(M)) on average 
