class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        m, n = len(nums), len(andValues)
        
        @cache
        def fn(i, j, mask): 
            """Return min sum at nums[j] and andValues[k] with given mask."""
            if i == m and j == n: return 0
            if i == m or j == n: return inf 
            mask &= nums[i]
            if mask < andValues[j]: return inf 
            if mask == andValues[j]: return min(fn(i+1, j, mask), nums[i] + fn(i+1, j+1, -1))
            return fn(i+1, j, mask)
            
        ans = fn(0, 0, -1)
        return ans if ans < inf else -1 