class Solution:
    def minimumCost(self, A: List[int], C: List[int], K: int) -> int:
        PA = list(accumulate(A, initial=0))
        PC = list(accumulate(C, initial=0))
        N = len(A)

        @cache
        def dp(i):
            if i == N:
                return 0

            ans = inf
            for j in range(i, N):
                cand = PA[j + 1] * (PC[j + 1] - PC[i])
                cand += K * (PC[-1] - PC[i])
                cand += dp(j + 1)
                ans = min(ans, cand)

            return ans

        return dp(0)