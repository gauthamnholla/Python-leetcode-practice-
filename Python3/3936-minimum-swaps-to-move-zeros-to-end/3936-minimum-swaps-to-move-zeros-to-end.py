class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
     a = 0
     j = len(nums)

     for i in range(j):
         if nums[i] == 0 and i < j - nums.count(0):
             a += 1
     return a
        
        