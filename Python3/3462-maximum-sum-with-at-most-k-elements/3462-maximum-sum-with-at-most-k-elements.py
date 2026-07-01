class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        a = []
        
        # For each row in the grid
        for i in range(len(grid)):
            # Sort the row in descending order
            s = sorted(grid[i], reverse=True)
            
            # Select top elements based on limits
            a.extend(s[:limits[i]])
        
        # Sort all selected elements in ascending order
        a.sort()
        
        s = 0
        
        # Pick the largest k elements and sum them up
        for i in range(k):
            s += a.pop()
        
        return s