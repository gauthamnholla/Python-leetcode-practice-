class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        invalid = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                invalid.add(fronts[i])
        check = []
        k = fronts + backs
        for j in k:
            if j not in invalid:
                check.append(j)
        if len(check) == 0:
            return 0
        return min(check)

        