class Solution(object):
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        slist = list(set(nums)) 
        slist.sort(reverse=True)
        return slist[:k]