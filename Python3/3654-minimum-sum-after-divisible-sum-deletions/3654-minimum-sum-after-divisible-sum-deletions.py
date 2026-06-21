class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:

        mx = lambda x, y: x if x > y else y
        n = len(nums) + 1
        
        dp, lastIdx = [0] * n, [None] * k
        lastIdx[0] = 0

        pref = list(accumulate(nums, initial = 0))

        for idx in range(1, n):

            dp[idx] = dp[idx - 1]
            mod = pref[idx] % k

            if lastIdx[mod] != None:
                prev = lastIdx[mod]
                dp[idx] = mx(dp[idx], (pref[idx]  - pref[prev]) + dp[prev])
            lastIdx[mod] = idx

        return pref[~0] - dp[~0]