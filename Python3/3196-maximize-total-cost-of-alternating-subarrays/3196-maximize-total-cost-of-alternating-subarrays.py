class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:

        dp1 = dp2 = nums.pop(0)                     # <-- 1)

        for n in nums:
            dp1, dp2 = max(dp1, dp2) + n, dp1 - n   # <-- 2)

        return max(dp1, dp2)                        # <-- 3)