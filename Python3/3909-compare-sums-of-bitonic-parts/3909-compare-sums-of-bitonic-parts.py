import numpy as np

class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        arr = np.array(nums)
    
        # In a strictly bitonic array, the peak is simply the maximum element.
        # np.argmax returns the index of that maximum element.
        peak_idx = np.argmax(arr)
    
        # Split the array using NumPy slicing. 
        # Remember: the peak element must be included in BOTH parts.
        ascending_part = arr[:peak_idx + 1]
        descending_part = arr[peak_idx:]
    
        # Vectorized summation
        sum_asc = np.sum(ascending_part)
        sum_desc = np.sum(descending_part)
    
        if sum_asc > sum_desc:
            return 0
        elif sum_desc > sum_asc:
            return 1
        else:
            return -1        