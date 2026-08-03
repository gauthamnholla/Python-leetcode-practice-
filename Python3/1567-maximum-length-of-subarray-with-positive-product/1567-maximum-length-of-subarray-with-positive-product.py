class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = pos = neg = 0
        for i in nums:
            if i == 0: # Case 1 -> Reset the subarrays
                pos = neg = 0
            elif i > 0: # Case 2 -> +ve subarray remains +ve and -ve remains -ve after adding the new value
                pos += 1 # increment pos
                neg = 0 if neg == 0 else neg + 1 # neg remains 0 if it is already 0 otherwise increment it.
            else: # Case 3 -> +ve subarray becomes -ve and -ve becomes +ve after adding the new value due to sign reversal.
                old_pos = pos
                pos = 0 if neg == 0 else neg + 1 # pos becomes 0 if it is neg is 0 otherwise it is neg+1
                neg = old_pos + 1 # neg becomes old pos + 1
            max_len = max(max_len, pos) # Update the max_len 
        return max_len 