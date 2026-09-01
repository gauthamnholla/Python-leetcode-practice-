class Solution:
    def maxPairStrength(self, nums: List[int]) -> int:
        ans = 0

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                g = gcd(nums[i], nums[j])
                ans = max(ans, nums[i] * nums[j] // (g * g))

        return ans