class Solution:
    def firstDigit(self, n: int) -> int:
        while n >= 10:
            n //= 10
        return n

    def countValidSubarrays(self, nums: List[int], x: int) -> int:
        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        ans = 0

        for i in range(n):
            for j in range(i, n):
                total = pref[j + 1] - pref[i]

                if total % 10 != x:
                    continue

                if self.firstDigit(total) == x:
                    ans += 1

        return ans