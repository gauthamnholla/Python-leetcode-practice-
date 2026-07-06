class Solution:
    MOD = 10**9 + 7

    def maxTotalValue(self, value: List[int], decay: List[int], m: int) -> int:
        n = len(value)

        def count_terms(x):
            cnt = 0

            for i in range(n):
                if value[i] < x:
                    continue

                cnt += (value[i] - x) // decay[i] + 1

                if cnt >= m:
                    return cnt

            return cnt

        lo, hi = 1, 10**9
        threshold = 0

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if count_terms(mid) >= m:
                threshold = mid
                lo = mid + 1
            else:
                hi = mid - 1

        total = 0
        used = 0

        for i in range(n):
            a = value[i]
            d = decay[i]

            if a <= threshold:
                continue

            cnt = (a - (threshold + 1)) // d + 1
            used += cnt

            last = a - (cnt - 1) * d
            total += cnt * (a + last) // 2

        remaining = m - used
        total += remaining * threshold

        return total % self.MOD