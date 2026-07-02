class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        @cache
        def dfs(i: int, sum: int) -> int:
            if sum == k:
                return pow(2, len(nums) - i, 1000000007)
            if sum > k or i >= len(nums):
                return 0
            return (2 * dfs(i + 1, sum) + dfs(i + 1, sum + nums[i])) % 1000000007
        return dfs(0, 0)