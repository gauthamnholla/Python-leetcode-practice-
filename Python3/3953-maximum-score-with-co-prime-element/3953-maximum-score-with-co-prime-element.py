class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        MAXA = max(max(nums), maxVal)

        mu = [0] * (MAXA + 1)
        mu[1] = 1
        primes = []
        is_comp = [False] * (MAXA + 1)

        for i in range(2, MAXA + 1):
            if not is_comp[i]:
                primes.append(i)
                mu[i] = -1
            for p in primes:
                v = i * p
                if v > MAXA:
                    break
                is_comp[v] = True
                if i % p == 0:
                    mu[v] = 0
                    break
                mu[v] = -mu[i]

        freq = [0] * (MAXA + 1)
        for x in nums:
            freq[x] += 1

        n = len(nums)
        cntMul = [0] * (MAXA + 1)
        for d in range(1, MAXA + 1):
            s = 0
            for m in range(d, MAXA + 1, d):
                s += freq[m]
            cntMul[d] = s

        coprimeAll = [0] * (MAXA + 1)
        for d in range(1, MAXA + 1):
            if mu[d] == 0:
                continue
            val = mu[d] * cntMul[d]
            for x in range(d, MAXA + 1, d):
                coprimeAll[x] += val

        ans = -10**18
        for x in range(1, MAXA + 1):
            bad = n - coprimeAll[x]

            if freq[x] > 0:
                cost = 0 if x == 1 else bad - 1
                ans = max(ans, x - cost)

            if x <= maxVal:
                cost = bad if bad > 0 else 1
                ans = max(ans, x - cost)

        return ans