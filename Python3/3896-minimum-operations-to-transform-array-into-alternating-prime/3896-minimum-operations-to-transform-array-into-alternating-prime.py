class Solution:
    n = 100004
    sieve = [1] * n
    sieve[0] = sieve[1] = 0

    for i in range(2, 317):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = 0

    def minOperations(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            j = nums[i]
            if i & 1:
                while self.sieve[j]:
                    res += 1
                    j += 1
            else:
                while not self.sieve[j]:
                    res += 1
                    j += 1

        return res