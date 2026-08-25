class Solution:
    def findNonMinOrMax(self, nums):
        # Intuition: check each num against every other num
        if len(nums) <= 2:
            return -1
        for i in range(len(nums)):
            isMin = True
            isMax = True
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    isMin = False
                if nums[j] > nums[i]:
                    isMax = False
            if not isMin and not isMax:
                return nums[i]
        return -1