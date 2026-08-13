class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        result = 0
        for i in range(n):
            subnums, subsum = set(), 0
            for j in range(i, n):
                subsum += nums[j]
                subnums.add(nums[j])
                result += int(subsum in subnums)

        return result