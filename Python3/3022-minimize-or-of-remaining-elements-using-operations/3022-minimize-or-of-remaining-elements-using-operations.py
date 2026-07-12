class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        mask = 0
        # iterate from highest bit 29 down to 0
        for bit in range(29, -1, -1):
            # mask has all previous removable bits set and the current one
            mask |= 1 << bit
            opsNeeded = 0
            andRes = 0
            # iterate over all numbers and count how many ops we need
            for x in nums:
                if andRes != 0:
                    andRes &= x
                    opsNeeded += 1
                elif x & mask != 0:
                    andRes = x & mask
            if andRes != 0: opsNeeded += 1
            # if we'd need to many ops, remove the bit from the mask
            if opsNeeded > k: mask -= 1 << bit
        # return the inverted mask
        return (1 << 30) - 1 - mask