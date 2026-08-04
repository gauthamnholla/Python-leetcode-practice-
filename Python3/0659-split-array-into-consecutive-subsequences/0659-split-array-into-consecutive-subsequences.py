class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = {}
        end = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for i in nums:
            if freq[i] == 0:
                continue

            if end.get(i-1, 0) > 0:
                end[i-1] -= 1
                end[i] = end.get(i, 0) + 1
                freq[i] -= 1
            elif freq.get(i+1, 0) > 0 and freq.get(i+2, 0) > 0:
                freq[i] -= 1
                freq[i+1] -= 1
                freq[i+2] -= 1
                end[i+2] = end.get(i+2, 0) + 1
            else:
                return False
        return True