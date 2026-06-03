class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:

        ans = 0
        pref = list(accumulate(damage, initial = 0))

        for i, (dmg, req) in enumerate(zip(pref[1:], requirement)):

            if dmg + req  <= hp:
                ans+= i + 1
            else:
                idx = bisect_left(pref, dmg + req - hp)
                if idx < i + 1:
                    ans+= i + 1 - idx 
        return ans