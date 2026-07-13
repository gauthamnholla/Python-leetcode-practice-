class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        return reduce(lambda tested, battery: tested + (battery > tested), batteryPercentages, 0)