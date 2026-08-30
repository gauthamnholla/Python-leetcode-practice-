class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        sl = SortedList([0])
        res = 0
        s = 0
        for x in nums:
            if x % 2:
                s += a
            else:
                s -= b

            res += sl.bisect_right(s)
            sl.add(s)
        return res