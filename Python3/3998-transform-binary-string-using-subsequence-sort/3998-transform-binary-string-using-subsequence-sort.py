class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        s0, s1 = s.count('0'), s.count('1')

        def test(t):
            t0, t1 = t.count('0'), t.count('1')
            if t0 > s0 or t1 > s1:
                return False
            t = t.replace('?', '0', s0 - t0).replace('?', '1')
            diff = 0
            for c1, c2 in zip(s, t):
                diff += int(c1) - int(c2)
                if diff < 0:
                    return False
            return True
        return [test(t) for t in strs]        