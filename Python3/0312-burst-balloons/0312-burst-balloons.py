class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(1)
        nums.insert(0, 1)
        @cache              # range in which we want to choose the last balloon to burst.
        def dp(start, end): # we know anything outside the range lasts "longer", as we determined it will burst later
            maxi = -(2 ** 31)
            if end < start:
                return 0

            for i in range(start, end + 1):
                maxi = max(maxi, dp(start, i - 1) + dp(i + 1, end) + nums[start - 1] * nums[i] * nums[end + 1])
            
            return maxi
        
        return dp(1, n)