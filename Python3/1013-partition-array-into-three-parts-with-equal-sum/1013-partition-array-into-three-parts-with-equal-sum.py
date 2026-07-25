class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        #partiton array in three equal parts 
        n=len(arr)
        tot=sum(arr)
        if tot%3!=0:
            return False
        pref=[0]*(n)
        for i in range(n):
            pref[i]=(pref[i-1] if i>0 else 0)+arr[i]
        #order matters 
        idx=-1
        for i in range(n):
            if  pref[i]==(tot//3):
                idx=i
                break
        if idx==-1:
            return False 
        for i in range(idx+1,n-1):
            if pref[i]==(2*tot)//3:
                return True
        return False