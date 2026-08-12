class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        dp = [0]*(budget)
        mx = 0
        for cap, cost in sorted(zip(capacity, costs), key = lambda x: x[1]):
            if cost >= budget:
                break
            if cost+cost < budget:
                mx = max(mx, dp[cost] + cap)
            dp[cost] = max(dp[cost], cap)

        mxs = [0]*(budget//2)
        for i in range(budget//2):
            mxs[i] = max(mxs[i-1], dp[i])

        
        for i in range(budget-1, 0,-1):
            mx = max(mx, dp[i] + mxs[min(budget-i-1,i-1)])
        return mx