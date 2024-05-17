# Beats 99.67%⌛✅🔥| Python💻| Clear Explanation📗

## 1. Proof
![image.png](https://assets.leetcode.com/users/images/81b35cda-7f9f-4723-b4a5-0a25d02206ae_1715913631.7686868.png)

## 2. Algorithms
- Depth-First Search

## 3. Code (Python3) - with explanation each line
```python3 []
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
```

## 4. Complexity
- Time complexity: $$O(N)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(H)$$ on average, $$O(N)$$ worst case (recursive stack calls)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
### Upvote [here](https://leetcode.com/problems/delete-leaves-with-a-given-value/solutions/5168079/beats-99-67-python-clear-explanation) if you find this solution helpful, thank you 🤍
