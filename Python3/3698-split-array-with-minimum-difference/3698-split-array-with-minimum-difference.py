class Solution:
    def splitArray(self, nums: List[int]) -> int:             
        # get index of maximum element (peak)
        maximum = nums.index(max(nums))

        # check if array is strictly increasing from start until peak
        for i in range(maximum):
            if nums[i] >= nums[i + 1]:
                return -1

        # check if array is strictly decreasing from peak until the end
        for i in range(maximum + 1, len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                return -1

        # compute the difference when there are 2 adjacent peaks. ex: [1, 2, 3, 3, 1]
        if maximum < len(nums) - 1 and nums[maximum] == nums[maximum + 1]:
            return abs(sum(nums[:maximum + 1]) - sum(nums[maximum + 1 :]))

        # compute the differences
        diff1 = abs(sum(nums[:maximum]) - sum(nums[maximum:]))
        diff2 = abs(sum(nums[:maximum + 1]) - sum(nums[maximum + 1:]))
        return min(diff1, diff2)