class Solution:
    def maximumScore(self, nums: List[int]) -> int:

        suff, pref = nums.pop(), sum(nums)  # <-- 1)
        ans = pref - suff

        while nums:                         # <-- 2)
            if  ans < pref - suff: 
                ans = pref - suff

            num = nums.pop()
            pref-= num                       
            if  suff > num:
                suff = num                  # <-- 3)

        return ans
    