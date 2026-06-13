from collections import deque

class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        def best_with(cost):
            dp = [(0, 0)] * (len(nums) + 1)
            best = (-10**30, 0)
            queue = deque()

            for i in range(1, len(nums) + 1):
                j = i - l
                if j >= 0:
                    candidate = (dp[j][0] - prefix[j], dp[j][1])
                    while queue and queue[-1][1] <= candidate:
                        queue.pop()
                    queue.append((j, candidate))

                while queue and queue[0][0] < i - r:
                    queue.popleft()

                if queue:
                    value, count = queue[0][1]
                    # take one valid subarray ending here
                    best = max(best, (value + prefix[i] - cost, count - 1))

                # either we have selected something or are still empty
                dp[i] = max(best, (0, 0))

            return best

        low, high = 0, sum(x for x in nums if x > 0) + 1

        while low < high:
            mid = (low + high) >> 1
            if -best_with(mid)[1] <= m:
                high = mid
            else:
                low = mid + 1

        value, _ = best_with(low)
        return value + low * m