class Solution:
    def minInitialStrength(self, monsters: List[int], boosts: List[List[int]]) -> int:
        n = len(monsters)
        diff = [0] * (n + 1)

        for l, r, v in boosts:
            diff[l] += v
            if r + 1 < len(diff):
                diff[r + 1] -= v

        bonus = [0] * n
        cur = 0

        for i in range(n):
            cur += diff[i]
            bonus[i] = cur

        need = 0

        for i in range(n - 1, -1, -1):
            if need == 0:
                need = max(0, monsters[i] - bonus[i])
            else:
                need += monsters[i]

        return need