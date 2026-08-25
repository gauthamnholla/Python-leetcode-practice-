class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        for i in range(len(grid)):
            d[int("".join(str(c) for c in grid[i]), 2)] = i+1
        if d[0] != 0: return [d[0]-1]
        for n1 in range(32):
            for n2 in range(32):
                if n1 & n2 == 0 and d[n1] != 0 and d[n2] != 0:
                    return sorted([d[n1]-1, d[n2]-1])
        return []