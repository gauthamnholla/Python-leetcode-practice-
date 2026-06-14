class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        intervals.sort()
        time=0
        st,end=intervals[0]
        for s,e in intervals[1:]:
            if (s<=end+1):
                end=max(end,e)
            else:
                time+=(end-st+1)
                st,end=s,e
        time+=end-st+1
        total=(brightness+2)//3
        return total*time