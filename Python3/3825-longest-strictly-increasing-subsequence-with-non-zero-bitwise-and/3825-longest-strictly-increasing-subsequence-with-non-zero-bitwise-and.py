mx = lambda x, y: x if x > y else y

class Solution:
    def longestSubsequence(self, nums):

        def lis(nums, bit):
            dp = []
            for num in nums:
                if bit & num == 0: continue
                i = bisect_left(dp, num)
                if i == len(dp): dp.append(num)
                else: dp[i] = num
            return len(dp)

        ans, bit = 0, 1
        mxBits = max(nums).bit_length()
        for i in range(mxBits):
            ans = mx(ans, lis(nums, bit))
            bit*= 2
        return ans