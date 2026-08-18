class Solution:
    def smallestAbsent(self, nums):
        freq = [False] * 201
        total = 0
        n = len(nums)
        for num in nums:
            total += num
            freq[num + 100] = True

        avg = total / n
        for i in range(1, 101):
            if not freq[i + 100] and avg < i:
                return i
        return 101