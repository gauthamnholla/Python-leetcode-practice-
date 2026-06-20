class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        dpi={"i":0,"p":0,"ii":0,"pp":0,"ip":0,"pi":0}
        
        l=nums
        n=len(l)

        for i in range(n):
            if i==0:
                if l[i]%2==0:
                    dpi["p"]+=1
                else:
                    dpi["i"]+=1
                continue
            if l[i]%2==0:
                dpi["pp"]+=dpi["p"]+dpi["ip"]
                dpi["ip"]+=dpi["i"]+dpi["ii"]+dpi["pi"]
                dpi["p"]+=1
                continue
            dpi["ii"]+=dpi["i"]+dpi["pi"]
            dpi["pi"]+=dpi["p"]+dpi["pp"]+dpi["ip"]
            dpi["i"]+=1
        
        return sum(dpi[k] for k in dpi)%(7+10**9)