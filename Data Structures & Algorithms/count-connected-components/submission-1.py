class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count
