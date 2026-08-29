class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n = len(nums)

        # depths[i] = depth of node i
        depths = [-1] * n

        def get_depth(i: int) -> int:
            # Already calculated
            if depths[i] != -1:
                return depths[i]

            # Root node
            if parent[i] == -1:
                depths[i] = 1
            else:
                # Depth = parent's depth + 1
                depths[i] = get_depth(parent[i]) + 1

            return depths[i]

        # Calculate depth of every node
        for i in range(n):
            get_depth(i)

        # Maximum depth = tree height
        height = max(depths)

        # Calculate weighted sum
        total_weight = 0

        for i in range(n):
            weight = height - depths[i] + 1
            total_weight += nums[i] * weight

        return total_weight