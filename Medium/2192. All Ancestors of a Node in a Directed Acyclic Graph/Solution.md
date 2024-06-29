## Efficiency
![image](https://github.com/KCP17/LeetCode-Solutions/assets/148914885/641b7173-175f-434f-b209-5bc2c3178df4)

## Code (Python3)
```python3 []
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def dfs(node, cur):
            visited.add(node)
            for nxt in src_dst[node]:
                cur.add(nxt)
                if nxt not in visited:
                    cur = dfs(nxt, cur)
            return cur
        
        res = []
        src_dst = [[] for _ in range(n)]
        for src, dst in edges:
            src_dst[dst].append(src)
        for node in range(n):
            visited = set()
            res.append(sorted(dfs(node, set())))
        return res
```
## Note:
DFS (My solution with hint used):
- Time: $$O(n^2 + n*log(n))$$
- Space: $$O(2n)$$ with `cur` and recursive depth
