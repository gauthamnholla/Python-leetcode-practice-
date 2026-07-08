mn = lambda num, y: num if num < y else y

class Solution:
    
    def minLength(self, nums: List[int], k: int) -> int:

        if sum(set(nums)) < k: return -1
        
        ctr = defaultdict(int)
        leftIdx, ans = 0, len(nums)

        for rghtIdx, rghtVal in enumerate(nums):
            if ctr[rghtVal] == 0:  k-= rghtVal
            ctr[rghtVal]+= 1
    
            while k <= 0:
                ans = mn(ans, rghtIdx - leftIdx + 1)
                leftVal = nums[leftIdx]
                ctr[leftVal]-= 1

                if ctr[leftVal] == 0: k+= leftVal
                leftIdx += 1
    
        return ans