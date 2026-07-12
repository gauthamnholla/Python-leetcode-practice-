class Solution:
    BASE = 3
    MOD = 1_000_000_000_000_000 - 11
    
    def hash(self, arr: list[int], start: int, end: int) -> int:
        h = 0
        for i in range(start, end):
            h = (h * self.BASE % self.MOD + arr[i]) % self.MOD
        return h
    
    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        n = len(pattern)        
        pattern_list = [x + 1 for x in pattern]
        target_hash = self.hash(pattern_list, 0, len(pattern_list))        
        base_pow = pow(self.BASE, n - 1, self.MOD)

        hills = [(b > a) - (b < a) + 1 for a, b in zip(nums, nums[1:])]        
        current_hash = self.hash(hills, 0, n)
        
        ans = int(target_hash == current_hash)        
        for i in range(n, len(hills)):
            current_hash = ((current_hash + self.MOD - hills[i - n] * base_pow % self.MOD) % self.MOD * self.BASE % self.MOD + hills[i]) % self.MOD
            ans += int(target_hash == current_hash)
        
        return ans