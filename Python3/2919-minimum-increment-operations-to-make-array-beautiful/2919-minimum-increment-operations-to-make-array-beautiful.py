
class Solution:
    def minIncrementOperations(self, nums, k):
        n = len(nums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            required = max(0, k - nums[i - 1])
            for j in range(i - 1, max(0, i - 3) - 1, -1):
                dp[i] = min(dp[j], dp[i])
            dp[i] += required

        result = min(dp[n], dp[n - 1], dp[n - 2])
        return result
