class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        return len(nums) % k == 0 and all(count <= len(nums) // k for count in Counter(nums).values())