class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        
        reachable = {}

        def dfs(node):
            if node in reachable:
                return reachable[node]
            
            reachable[node] = {node}
            for neighbour in adj[node]:
                reachable[node] |= dfs(neighbour)
            
            return reachable[node]
        
        for i in range(numCourses):
            dfs(i)

        result = []
        for u, v in queries:
            result.append(v in reachable[u])
        return result