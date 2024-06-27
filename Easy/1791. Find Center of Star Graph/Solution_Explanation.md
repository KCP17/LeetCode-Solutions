# Beats 98.90%✅🔥🔥| Python💻| CLEAR, CONCISE Explanation📗

## 1. Proof (Python3)
<!-- Describe your first thoughts on how to solve this problem. -->
![image.png](https://assets.leetcode.com/users/images/b1cac041-0ab8-4b57-b47c-725d3943b035_1719498994.4270878.png)

## 2. Algorithms
* Hash Set

## 3. Code - Python3 (with explanation)
```python3 []
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        '''
        Only the center node can be connected to more than 1 node
        In other words, only the center node can be a part of more than 1 edge
        So, if we see a node exists in more than 1 edge, that's the center node
        We initialize a HashSet and loop through the edges
        At each edge, we check if we've seen that node before (both nodes of that edge)
        - If yes then that's the center node
        - Else we add that (those) node(s) to the `seen` HashSet so we'll know that we've seen that (those) node(s) before when we get to the same node(s) later, and return that center node
        '''
        seen = set()
        for u, v in edges:
            if u in seen:
                return u
            if v in seen:
                return v
            seen.add(u)
            seen.add(v)
```

## 4. Complexity
- Time complexity: $$O(N)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(N)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Upvote [here](https://leetcode.com/problems/find-center-of-star-graph/solutions/5378501/beats-98-90-python-clear-concise-explanation) if you find this solution helpful, thank you 🤍
