class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
    
        # dp[i][j] means the longest subsequence ending at index i with at most j changes
        dp = [[1] * (k + 1) for _ in range(n)]
        
        for i in range(n):
            for j in range(k + 1):
                for l in range(i):
                    if nums[i] == nums[l]:
                        dp[i][j] = max(dp[i][j], dp[l][j] + 1)
                    elif j > 0:
                        dp[i][j] = max(dp[i][j], dp[l][j - 1] + 1)
    
        return max(max(row) for row in dp)
        