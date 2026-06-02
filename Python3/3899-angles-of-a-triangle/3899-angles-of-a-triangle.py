class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:

        a, b, c = sides

        # triangle inequality
        if a + b <= c or b + c <= a or c + a <= b:
            return []

        A = math.degrees(math.acos((b*b + c*c - a*a) / (2*b*c)))
        B = math.degrees(math.acos((a*a + c*c - b*b) / (2*a*c)))
        C = math.degrees(math.acos((a*a + b*b - c*c) / (2*a*b)))

        ans = [A, B, C]
        ans.sort()
        return ans