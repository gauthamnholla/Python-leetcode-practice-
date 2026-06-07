class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        
        n=len(nums2)
        k=int(n**0.5)+1

        base=[0]*n
        pfs=[]
        for i in range(n):
            if i%k==0:
                pfs+=defaultdict(int),
            else:
                pfs+=pfs[-1],
            pfs[-1][nums2[i]]+=1

        def add(x, y, val):
            while x%k!=0 and x<=y:
                pfs[x][nums2[x]]-=1
                pfs[x][nums2[x]+val]+=1
                nums2[x]+=val
                x+=1
            while y%k!=k-1 and x<=y:
                pfs[y][nums2[y]]-=1
                pfs[y][nums2[y]+val]+=1
                nums2[y]+=val
                y-=1
            while x<y:
                base[x]+=val
                x+=k

        def query(q):
            ans=0

            x=0
            y=n-1
            
            base_y=base[y - (y%k)]
            ans+=pfs[y][q-base_y]
            y-=((y%k)+1)
                
            while x<y:
                base_x=base[x]
                ans+=pfs[x][q-base_x]
                x+=k
            return ans

        ans=[]
        for q in queries:
            if q[0] == 2:
                cur=0
                for v in nums1:
                    cur += query(q[1] - v)
                ans+=cur,
            else:
                add(q[1], q[2], q[3])

        return ans