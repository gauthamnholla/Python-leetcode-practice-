class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        freq = Counter()
        for x in nums: 
            for p in range(2, isqrt(x)+1): 
                while x % p == 0: 
                    freq[p] += 1
                    x //= p 
            if x > 1: freq[x] += 1
        ovlp = 0 
        prefix = Counter()
        for i, x in enumerate(nums): 
            if i <= len(nums)-2: 
                for p in range(2, isqrt(x)+1): 
                    if x % p == 0: 
                        if prefix[p] == 0: ovlp += 1
                        while x % p == 0: 
                            prefix[p] += 1
                            x //= p 
                        if prefix[p] == freq[p]: ovlp -= 1
                if x > 1: 
                    if prefix[x] == 0: ovlp += 1
                    prefix[x] += 1
                    if prefix[x] == freq[x]: ovlp -= 1
                if not ovlp: return i 
        return -1 