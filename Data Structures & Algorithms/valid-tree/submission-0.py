class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited:
                    return False
                if not dfs(neighbour, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        
        return len(visited) == n
