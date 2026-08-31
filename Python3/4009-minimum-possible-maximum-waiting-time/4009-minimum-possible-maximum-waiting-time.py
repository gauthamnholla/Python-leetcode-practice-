class Solution:
    def minMaxWaitingTime(self, demand: List[int], fuel: List[int]) -> int:
        n = len(demand)

        def check(wait_limit: int) -> int:
            states = {(fuel[0], fuel[1], 0, 0)}

            served = 0

            for i in range(n):
                nxt = set()

                for f0, f1, t0, t1 in states:
                    if f0 >= demand[i]:
                        delay = t0
                        if delay <= wait_limit:
                            nxt.add((f0 - demand[i], f1, demand[i], max(0, t1 - delay)))

                    if f1 >= demand[i]:
                        delay = t1
                        if delay <= wait_limit:
                            nxt.add((f0, f1 - demand[i], max(0, t0 - delay), demand[i]))

                if not nxt:
                    break

                states = nxt
                served += 1

            return served

        mx = check(10**9)

        if mx == 0:
            return -1

        lo, hi = 0, sum(demand)
        ans = hi

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(mid) == mx:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans