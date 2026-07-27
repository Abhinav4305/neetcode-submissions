class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        state = [0] * numCourses

        def dfs(crs):
            if state[crs] == 1:
                return True
            elif state[crs] == 2:
                return False
            
            state[crs] = 1

            for pre in adj[crs]:
                if dfs(pre):
                    return True
                
            state[crs] = 2
            return False
        for i in range(numCourses):
            if dfs(i):
                return False
        return True
