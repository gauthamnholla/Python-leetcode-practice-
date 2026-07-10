class Solution:
    def maxScore(self, nums: List[int]) -> int:
        from math import gcd, lcm
        lm = nums[0]
        gd = nums[0]
        maxi = -float('inf')
        n = len(nums)

        for i in range(1, n):
            lm = lcm(lm, nums[i])
            gd = gcd(gd, nums[i])
        maxi = max(maxi, lm*gd)

        if n == 1:
            return maxi
            
        for i in range(n):
            tmp = nums[:i] + nums[i+1:]
            lm = tmp[0]
            gd = tmp[0]
            for j in range(1, len(tmp)):
                lm = lcm(lm, tmp[j])
                gd = gcd(gd, tmp[j])
            maxi = max(maxi, lm*gd)

        return maxi
        