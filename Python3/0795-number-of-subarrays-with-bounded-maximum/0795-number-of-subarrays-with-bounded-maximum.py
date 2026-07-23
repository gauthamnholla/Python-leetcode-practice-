class Solution:
    def numSubarrayBoundedMax(self, a: List[int], l: int, r: int) -> int:
        res = 0
        for _,g in groupby(a, lambda v:v<=r):
            if _ == 0: continue

            lastInRange = -1
            for i,v in enumerate(g):
                if l <= v <= r:
                    lastInRange = i

                res += lastInRange+1
        
        return res