class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        NEG = -4 * 10**18
        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        dp = [[NEG] * (n + 1) for _ in range(m + 1)]

        # Base case
        for i in range(n + 1):
            dp[0][i] = 0

        ans = NEG

        for t in range(1, m + 1):
            dq = deque()

            for i in range(1, n + 1):

                # Skip i-th position
                dp[t][i] = dp[t][i - 1]
                pos = i - l  # new element entering the window

                if pos >= 0:
                    val = dp[t - 1][pos] - pref[pos]

                    # Maintain decreasing order
                    while dq:
                        last = dq[-1]
                        if dp[t - 1][last] - pref[last] >= val:
                            break
                        dq.pop()

                    dq.append(pos)

                # Remove expired indices
                while dq and dq[0] < i - r:
                    dq.popleft()

                if dq:
                    start = dq[0]
                    candidate = dp[t - 1][start]- pref[start]+ pref[i]
                    dp[t][i] = max(dp[t][i], candidate)

            ans = max(ans, dp[t][n])

        return ans