class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])

        maxSide = 0
        maxK = min(m, n)
        minBottom = [float('inf')] * (maxK + 1)
        minRight = [float('inf')] * (maxK + 1)
        maxLeft = [float('-inf')] * (maxK + 1)
        for i in range(m):
            for j in range(n):
                k = dp[i][j]

                if k == 0:
                    continue

                top = i - k + 1
                bottom = i
                left = j - k + 1
                right = j

                if ((minBottom[k] < top) or (minRight[k] < left) or (right < maxLeft[k])):
                    maxSide = max(maxSide, k)

                minBottom[k] = min(minBottom[k], bottom)
                minRight[k] = min(minRight[k], right)
                maxLeft[k] = max(maxLeft[k], left)

        maxArea = maxSide * maxSide
        return maxArea