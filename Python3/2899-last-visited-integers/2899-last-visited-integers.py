class Solution(object):
    def lastVisitedIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = []
        ans = []
        k = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                seen.insert(0,nums[i])
                k = 0
            else:
                k += 1
                if k > len(seen):
                    ans.append(-1)
                else:
                    ans.append(seen[k-1])
        return ans
        