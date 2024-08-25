## 1. Efficiency (Python3)
![image](https://github.com/user-attachments/assets/abdb0ed9-8011-4457-841b-858fd9e19b48)

## 2. Code (Python3)
```python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Traverse the left child -> right child -> parent
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            self.res.append(node.val)

        self.res = []
        dfs(root)
        return self.res
```

## 3. Note:
DFS (My solution) - has not met follow-up requirements yet:
- Time: $$O(n)$$
- Space: $$O(n)$$
