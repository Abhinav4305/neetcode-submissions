class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        n = len(edges)
        visited = set()

        edges.sort()
        visited.add(edges[0][0])
        visited.add(edges[0][1])
        count = 1

        for i in range(n):
            if edges[i][0] in visited:
                visited.add(edges[i][1])
            elif edges[i][1] in visited:
                visited.add(edges[i][0])
            else:
                count += 1
        return count



        
