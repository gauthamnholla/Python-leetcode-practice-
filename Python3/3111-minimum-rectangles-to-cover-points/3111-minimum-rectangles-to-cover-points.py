class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
    
        x = sorted(list(zip(*points))[0])
        n, cnt, ptr = len(x), 0, 0

        while ptr < n:
            ptr = bisect_right(x, x[ptr]+w, lo = ptr)
            cnt+= 1
     
        return cnt