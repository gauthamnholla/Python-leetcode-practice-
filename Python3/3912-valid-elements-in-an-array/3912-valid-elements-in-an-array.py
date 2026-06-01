class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        leftgreat=[0]*n
        rightgreat=[0]*n
        res=[]
        if n==1:
            return[nums[0]]
        for i in range(n):
            if i==0:
                leftgreat[i]=0
            else:
                leftgreat[i]=max(nums[i-1],leftgreat[i-1])
            j=n-i-1
            if j==n-1:
                rightgreat[j]=0
            else:
                rightgreat[j]=max(nums[j+1],rightgreat[j+1])
        for i in range(n):
            if i==0 or i==n-1 or nums[i]>leftgreat[i] or nums[i]>rightgreat[i]:
                res.append(nums[i])
        return res