# Beats 95.83%⌛✅| Python💻| Clear Explanation📕

## 1. Proof
![image.png](https://assets.leetcode.com/users/images/e81ae07c-08bc-4277-9067-11ae6d373423_1715848871.5667922.png)

## 2. Algorithms
- Depth-First Search

## 3. Code (Python3) - with concise explanation each line
```python3 []
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
```

## 4. Complexity
- Time complexity: $$O(N)$$ worst case
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(H)$$ on average - with `H` height of the tree, $$O(N)$$ worst case
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
### Upvote [here](https://leetcode.com/problems/evaluate-boolean-binary-tree/solutions/5164622/beats-95-83-python-clear-explanation) if you find this solution helpful, thank you 🤍
