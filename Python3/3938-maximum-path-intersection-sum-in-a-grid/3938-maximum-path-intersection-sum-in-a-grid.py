class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        maxSum = -float('inf')

        for i in range(1, n - 1) :
            for j in range(1, m - 1) :
                maxSum = max(maxSum, grid[i][j])

        for i in range(n) :
            curSum = grid[i][0]
            for j in range(1, m) :
                curSum = max(curSum + grid[i][j], grid[i][j] + grid[i][j - 1])
                maxSum = max(maxSum, curSum)

        for j in range(m) :
            curSum = grid[0][j]
            for i in range(1, n) :
                curSum = max(curSum + grid[i][j], grid[i][j] + grid[i - 1][j])
                maxSum = max(maxSum, curSum)

        return maxSum  
