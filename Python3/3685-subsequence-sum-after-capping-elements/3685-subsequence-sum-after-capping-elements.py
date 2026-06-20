class Solution(object):
    def subsequenceSumAfterCapping(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[bool]
        """
        nums.sort()
        
        # Frequency map
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        reachable_sums = {0}
        n = len(nums)
        processed_count = 0
        can_cap = [False] * n
        
        for length in range(1, n + 1):
            remainder = k % length
            count_of_this_value = frequency.get(length, 0)
            
            # Check feasibility
            while remainder <= k:
                if remainder in reachable_sums:
                    remaining = k - remainder
                    available_elements = n - processed_count
                    if remaining % length == 0 and remaining // length <= available_elements:
                        can_cap[length - 1] = True
                        break
                remainder += length
            
            # Expand reachableSums reachable sums
            new_sums = set()
            current_value = length
            for _ in range(count_of_this_value):
                for s in reachable_sums:
                    if s + current_value <= k:
                        new_sums.add(s + current_value)
                current_value += length
            
            reachable_sums.update(new_sums)
            processed_count += count_of_this_value
        
        return can_cap