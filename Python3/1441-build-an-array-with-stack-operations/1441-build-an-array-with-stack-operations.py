class Solution:
    def buildArray(self, a: List[int], n: int) -> List[str]:
        res=[]
        c=0
        for i in range(1,n+1):
            res.append("Push")
            if a[c]!=i:
                res.append("Pop")
            else:
                c+=1
            i+=1
            if c>=len(a):
                break
        return res