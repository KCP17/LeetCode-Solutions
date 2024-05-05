## 1. Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/3791c1d4-1b3f-4cba-b47b-b025195d6cae)

## 2. Code (Python3) - with explanation each line
```python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int: # Basic DFS
        def dfs(node, cur_num, res): # Search every path and accumulate the result at each path's leaf            
            if node.left: # Search on the left
                res = dfs(node.left, cur_num + str(node.val), res)
            if node.right: # Search on the right
                res = dfs(node.right, cur_num + str(node.val), res)
            if not node.left and not node.right: # If standing at the leaf
                res += int(cur_num + str(node.val)) # Add the current result with the recent represented number
            
            return res
        
        return dfs(root, "", 0)
```
## 3. Note:
DFS (My solution):
- Time: $$O(N)$$ with N nodes
- Space: $$O(H)$$ with H height of the tree or recursive depth
