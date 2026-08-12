class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        for i in reversed(range(1, len(nums))):
            if nums[i - 1] >= nums[i]:
                return i
        return 0