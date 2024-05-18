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
