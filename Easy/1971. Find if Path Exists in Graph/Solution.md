## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/8ce04fb0-4e14-484f-9e99-61cc923837ea)

## Code (Python3)
```python3 []
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(src):
            if src == destination:
                return True
            
            while graph[src]:
                dst = graph[src].pop()
                if dfs(dst):
                    return True
            
            return False

        graph = [[] for _ in range(n)]
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        
        return dfs(source)
```
## Note:
DFS (My solution):
- Time: $$O(2n)$$ roughly
- Space: $$O(n)$$
