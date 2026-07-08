class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        totalCount = defaultdict(int)

        for g in group:
            totalCount[g] += 1

        ans = 0

        def dfs(node, parent):

            nonlocal ans

            freq = defaultdict(int)
            freq[group[node]] = 1

            for nei in graph[node]:

                if nei == parent:
                    continue

                childFreq = dfs(nei, node)

                for g, cnt in childFreq.items():

                    ans += (
                        cnt
                        * (
                            totalCount[g]
                            - cnt
                        )
                    )

                # small-to-large merge
                if len(childFreq) > len(freq):
                    freq, childFreq = (
                        childFreq,
                        freq
                    )

                for g, cnt in childFreq.items():
                    freq[g] += cnt

            return freq

        dfs(0, -1)

        return ans