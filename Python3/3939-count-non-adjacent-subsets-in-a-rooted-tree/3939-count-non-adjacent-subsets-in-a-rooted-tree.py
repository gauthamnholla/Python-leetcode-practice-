import numpy as np
from scipy.signal import fftconvolve

class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        MOD = 1000000007
        SHIFT = 15
        BASE = 1 << SHIFT
        MASK = BASE - 1
        BASE1 = BASE % MOD
        BASE2 = (BASE * BASE) % MOD

        n = len(parent)
        children = [[] for _ in range(n)]
        root = 0
        for i, p in enumerate(parent):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        order = []
        st = [(root, 0)]
        while st:
            u, seen = st.pop()
            if seen:
                order.append(u)
            else:
                st.append((u, 1))
                for v in children[u]:
                    st.append((v, 0))

        vals = [x % k for x in nums]

        def conv(a, b):
            a0 = (a & MASK).astype(np.float64)
            a1 = (a >> SHIFT).astype(np.float64)
            b0 = (b & MASK).astype(np.float64)
            b1 = (b >> SHIFT).astype(np.float64)

            p = fftconvolve(a0 + 1j * a1, b0 + 1j * b1)
            q = fftconvolve(a0 + 1j * a1, b0 - 1j * b1)

            pr = np.rint(p.real).astype(np.int64)
            pi = np.rint(p.imag).astype(np.int64)
            qr = np.rint(q.real).astype(np.int64)

            x = (pr + qr) >> 1
            z = (qr - pr) >> 1
            y = pi

            c = (x % MOD + (y % MOD) * BASE1 + (z % MOD) * BASE2) % MOD
            res = c[:k].copy()
            if k > 1:
                res[:k - 1] += c[k:]
                res %= MOD
            return res.astype(np.int64)

        dp0 = [None] * n
        dp1 = [None] * n

        for u in order:
            take = np.zeros(k, dtype=np.int64)
            leave = np.zeros(k, dtype=np.int64)
            take[0] = 1
            leave[0] = 1

            for v in children[u]:
                take = conv(take, dp0[v])
                child_all = (dp0[v] + dp1[v]) % MOD
                leave = conv(leave, child_all)

            s = vals[u]
            cur = np.zeros(k, dtype=np.int64)
            cur[(np.arange(k) + s) % k] = take

            dp0[u] = leave
            dp1[u] = cur

        return int((dp0[root][0] + dp1[root][0] - 1) % MOD)