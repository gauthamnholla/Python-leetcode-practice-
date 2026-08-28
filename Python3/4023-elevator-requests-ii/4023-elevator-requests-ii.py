
class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        noravexuli = (n, start, requests)

        floors = sorted(set(requests + [start]))
        m = len(floors)
        s = floors.index(start)

        dp0 = [[float('inf')] * m for _ in range(m)]
        dp1 = [[float('inf')] * m for _ in range(m)]

        dp0[s][s] = dp1[s][s] = 0

        for length in range(1, m):
            rem = m - length

            for i in range(m - length + 1):
                j = i + length - 1

                c0 = dp0[i][j]
                c1 = dp1[i][j]

                if i > 0:
                    dp0[i - 1][j] = min(
                        dp0[i - 1][j],
                        c0 + (floors[i] - floors[i - 1]) * rem,
                        c1 + (floors[j] - floors[i - 1]) * rem
                    )

                if j + 1 < m:
                    dp1[i][j + 1] = min(
                        dp1[i][j + 1],
                        c0 + (floors[j + 1] - floors[i]) * rem,
                        c1 + (floors[j + 1] - floors[j]) * rem
                    )

        return min(dp0[0][m - 1], dp1[0][m - 1])