class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        n = len(types)
        
        @lru_cache(None)
        def dfs(i, total):
            if total == target:
                return 1
            if i == n or total > target:
                return 0
            
            res = 0
            for j in range(types[i][0]):
                next_total = total + types[i][1] * (j + 1)
                if j == 0:
                    res += dfs(i + 1, total) # cover case for no marks
                res += dfs(i + 1, next_total)
                
            return res
        
        return dfs(0, 0) % (10**9 + 7)