class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], CI: List[int]) -> int:
        m = len(CI)
        n = len(nums)
        
        CI = [x-1 for x in CI]

        
        for ans in range(1,m+1):
            last = [-1]*n
            
            for i in range(ans):
                last[CI[i]] = i

            if last[0] ==-1:continue 
                
            mark = 0
            cnt = 0 
            
            for s in range(ans):
                if s == last[CI[s]]: 
                    if cnt>=nums[CI[s]]:
                        cnt-=nums[CI[s]]
                        mark+=1
                    else: 
                        break
                else: 
                    cnt+=1 
                    
            
            if mark == n: 
                return ans
            

        return -1