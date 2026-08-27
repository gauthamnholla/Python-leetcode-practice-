class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        g = max(lights)
        return max((period - r for t in arrivalTime if (r := t % period) >= g), default=0)