class Solution:
    def longestAlternatingSubarray(self, v, k):
        ans = 0
        for i in range(len(v)):
            ct = 0
            if (v[i] % 2 == 0) and (v[i] <= k):
                ct = 1
                for j in range(i + 1, len(v)):
                    if (v[j] % 2 == v[j - 1] % 2) or v[j] > k:
                        break
                    ct += 1
            ans = max(ans, ct)
        return ans
