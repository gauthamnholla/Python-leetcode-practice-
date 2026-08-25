class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:

        if 1 not in nums: return 0
        ans, digits = 1, 1

        nums = deque(nums)
        while nums[ 0] == 0: nums.popleft()
        while nums[-1] == 0: nums.pop()

        for num in nums:

            if num == 1:
                ans*= digits  
                ans%= 1_000_000_007
                digits = 0

            digits+= 1

        return ans