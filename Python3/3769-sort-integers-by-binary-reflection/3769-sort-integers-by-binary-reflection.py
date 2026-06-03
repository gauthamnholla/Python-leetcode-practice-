class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def reflection(x):
            b = bin(x)[2:]

            r = b[::-1]

            # remove leading zeros after reverse
            r = r.lstrip('0')

            val = int(r, 2) if r else 0

            return (val, x)

        nums.sort(key=reflection)

        return nums