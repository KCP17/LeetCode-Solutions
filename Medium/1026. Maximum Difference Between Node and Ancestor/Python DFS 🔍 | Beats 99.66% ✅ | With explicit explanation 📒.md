# Proof
<!-- Describe your first thoughts on how to solve this problem. -->
![image.png](https://assets.leetcode.com/users/images/eab5cc38-86df-4233-8363-8402fc60410b_1704972560.2389817.png)

# Illustration & Intuition
![Max difference between node & ancestor.jpg](https://assets.leetcode.com/users/images/c5f1024c-c80f-4503-bd1f-8c41c2c474dd_1704974453.3632424.jpeg)
## Depth-First Search:
1. Go deep into the red path and find the max difference of red path is 7.
2. Same process goes for the remaining paths.
3. The result is the max difference of all paths. Since ancestors & children belong to 1 path, we found all paths and got the maximum difference out of them.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Using depth-first search. First recursive call on the ``dfs()`` function with the ``root node``, ``empty list (family)``, ``difference = 0``.
2. Append the nodes along a path recursively (if the left node of current node exists then goes to it, same for the right node).
3. If both left & right nodes don't exist, means that we've reached the dead end of a path, thus find the maximum difference of the path based on max & min values of that path.
4. Going back (returning) and popping the nodes until we find the next path to go, then repeating from step 2.
5. When reaches dead end of the last path, we get the maximum difference out of the max differences of all paths, that is the result.

# Complexity
- Time complexity: $$O(n)$$ since we traverse through every node.

- Space complexity: $$O(h)$$ with h is the height of the tree due to recursive stack calls.

# Code (Python3)
```python3 []
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, family, diff):
            family.append(node.val) # family is a list of nodes belong to a path, keep appending as searching occurs
            
            if node.left is not None: # Search on the left if it exists
                diff = dfs(node.left, family, diff)
            if node.right is not None: # Search on the right if it exists
                diff = dfs(node.right, family, diff)

            if node.left is None and node.right is None: # When reaches dead end of a path
                diff = max(diff, max(family) - min(family)) # Find max, min of a path; subtract to get the difference -> get max between previous diff & current diff
            
            family.pop() # Remove the current node until we can move on to next path
            return diff

        return dfs(root, [], 0)
```
## Upvote if you find this solution helpful, thank you 🤍
