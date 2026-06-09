class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        flips = 0
        
        while i < n:
            nums[i] = 1 - nums[i] if flips % 2 == 1 else nums[i]
            
            if nums[i] == 0:
                flips += 1
            
            i += 1
        
        return flips