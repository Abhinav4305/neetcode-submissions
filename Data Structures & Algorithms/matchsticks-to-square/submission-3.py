class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4 != 0 :
            return False
        
        target = sum(matchsticks)//4
        matchsticks.sort(reverse = True)

        if matchsticks[0] > target:
            return False

        sides = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                return True 
            
            matchstick = matchsticks[i]

            for j in range(4):
                if sides[j] + matchstick <= target:
                    sides[j] += matchstick
                    if dfs(i + 1):
                        return True
                    sides[j] -= matchstick
            return False
        return dfs(0)
        