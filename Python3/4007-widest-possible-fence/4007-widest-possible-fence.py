class Solution:
    def maximumWidth(self, planks: List[int]) -> int:

        freq = Counter(planks)
        vals = list(freq.keys())
        pairs = defaultdict(int)

        m = len(vals)

        for i in range(m):
            for j in range(i, m):
                s = vals[i] + vals[j]
                if i == j:
                    pairs[s] += freq[vals[i]] // 2
                else:
                    pairs[s] += min(freq[vals[i]], freq[vals[j]])

        ans = 0

        for h, cnt in pairs.items():
            ans = max(ans, cnt + freq.get(h, 0))

        for cnt in freq.values():
            ans = max(ans, cnt)

        return ans