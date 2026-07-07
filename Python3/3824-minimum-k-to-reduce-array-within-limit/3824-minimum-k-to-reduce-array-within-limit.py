class Solution:
    def minimumK(self, nums: List[int]) -> int:
        def ok(K: int) -> bool:
            total = 0
            for u in nums:
                total += (u + K - 1) // K 
            return total <= K * K

        low, high = 1, 10**9
        while low < high:
            mid = (low + high) // 2
            if ok(mid):
                high = mid
            else:
                low = mid + 1

        return low