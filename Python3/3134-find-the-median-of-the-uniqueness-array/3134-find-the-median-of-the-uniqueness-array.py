class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        need = (((n*(n+1))//2 )+ 1) //2
        
        def count(x): 
            R = 0
            st = defaultdict(int)
            cnt = 0
            
            for L in range(n):
                while R<n:  
                    if nums[R] not  in st and len(st) == x: 
                        break                 
                    st[nums[R]]+=1 
                    R+=1
                
                cnt += R-L 
                
                st[nums[L]]-=1 
                if st[nums[L]] == 0:
                    del st[nums[L]]
                 
                
            return cnt<need

        l,r = 0,n+3            
        while l+1<r: 
            m = (l+r)>>1 
            
            if count(m): 
                l = m 
            else: 
                r = m
                
        return r