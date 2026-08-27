class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        n = len(requests)

        @cache
        def fn(i, msk):
            ar, fl = requests[i]
            if msk == (1<<n)-1: return max(abs(start-fl), ar)
            res = 1<<60
            for j in range(n):
                if msk&(1<<j): continue
                nar, nfl = requests[j]
                fdif = abs(nfl-fl)
                a = fn(j, msk|(1<<j))
                res = min(res, max(a+fdif, ar))

            return res

        res = [fn(i, 1<<i) for i in range(n)]
        return min(res)