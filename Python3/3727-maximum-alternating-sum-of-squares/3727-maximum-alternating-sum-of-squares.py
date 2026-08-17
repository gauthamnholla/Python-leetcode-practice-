class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        # square all elements
        s = sorted([x*x for x in nums])
        # sum of smaller half (to subtract)
        ns = sum(s[:n//2])
        # sum of larger half (to add)
        ps = sum(s[n//2:])
        return ps - ns