class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        positions, values = [], []
        for i, num in enumerate(nums):
            if num >= 0:
                positions.append(i)
                values.append(num)

        if len(positions) == 0:
            return nums

        k = k % len(positions)
        values = values[k:] + values[:k] 
        for i, val in zip(positions, values):
            nums[i] = val

        return nums