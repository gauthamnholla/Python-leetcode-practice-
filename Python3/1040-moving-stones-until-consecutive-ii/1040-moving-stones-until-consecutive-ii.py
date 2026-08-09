class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        N = len(stones)
        stones.sort()
        mx = sum(stones[i]-stones[i-1]-1 for i in range(1, N-1))

        mx = max(mx, sum((stones[i]-stones[i-1]-1) for i in range(2, N)))


        mn = 10 ** 12


        l = 0

        for r in range(N):

            while stones[r]-stones[l]+1>N:
                l+=1

            
            amt = r-l+1
            left = N-amt

            if left == 1 and stones[r] - stones[l] + 1 == N-1:
                left = 2

            mn = min(mn, left)

        return [mn, mx]