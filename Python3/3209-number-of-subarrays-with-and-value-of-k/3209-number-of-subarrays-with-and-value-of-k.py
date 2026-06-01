class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        subarray_counts = {}
        total_subarrays = 0

        for num in nums:
            new_counts = {}
            for subarray_and, freq in subarray_counts.items():
                new_and = subarray_and & num
                new_counts[new_and] = new_counts.get(new_and, 0) + freq

            new_counts[num] = new_counts.get(num, 0) + 1
            subarray_counts = new_counts

            total_subarrays += subarray_counts.get(k, 0)

        return total_subarrays