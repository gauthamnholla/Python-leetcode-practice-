class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:

        ans = deque()
        pow10 = 1

        while n:
            n, digit = divmod(n, 10)        # <-- 1)
            component = digit * pow10
            pow10*= 10

            if component == 0: continue     # <-- 2)
            ans.appendleft(component)

        return list(ans)