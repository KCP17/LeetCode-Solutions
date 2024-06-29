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
