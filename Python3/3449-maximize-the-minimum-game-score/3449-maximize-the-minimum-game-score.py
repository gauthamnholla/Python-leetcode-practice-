class Solution:
    def maxScore(self, A: List[int], M: int) -> int:
        N = len(A)

        def possible(bound):
            req = [(bound + x - 1) // x for x in A]
            steps = 0
            for i, x in enumerate(req):
                if x:
                    steps += 2 * x - 1
                    if i + 1 < N:
                        req[i + 1] = max(0, req[i + 1] - (req[i] - 1))
                elif i < N - 1:
                    steps += 1
            return steps <= M

        lo, hi = 0, int(10**6 * M / N) + 1
        while lo < hi:
            mi = lo + hi + 1 >> 1
            if possible(mi):
                lo = mi
            else:
                hi = mi - 1
        return lo