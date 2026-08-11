class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        INF = 10**15
        dp = [[[-1, -1] for _ in range(n)] for _ in range(m)]
        return 1 + self.f(0, 0, 1, waitCost, dp)

    def f(self, i: int, j: int, parity: int, waitCost: List[List[int]], dp: List[List[List[int]]]) -> int:
        m, n = len(waitCost), len(waitCost[0])
        if i == m - 1 and j == n - 1:
            return 0
        if i < 0 or i >= m or j < 0 or j >= n:
            return 10**15
        if dp[i][j][parity] != -1:
            return dp[i][j][parity]
        ans = 10**15
        if parity == 1:
            ans = min(ans, (i + 2) * (j + 1) + self.f(i + 1, j, 0, waitCost, dp))
            ans = min(ans, (i + 1) * (j + 2) + self.f(i, j + 1, 0, waitCost, dp))
        else:
            ans = min(ans, waitCost[i][j] + self.f(i, j, 1, waitCost, dp))
        dp[i][j][parity] = ans
        return ans