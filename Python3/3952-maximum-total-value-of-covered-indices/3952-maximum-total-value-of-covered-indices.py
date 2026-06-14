class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        preidx=-1
        n=len(s)
        ans=0
        for i in range(n):
            if s[i]=='1':
                if preidx==-1 or nums[i]>=nums[preidx]:
                    ans+=nums[i]
                else:
                    ans+=nums[preidx]
                    preidx=i
            else:
                preidx=i
        return ans