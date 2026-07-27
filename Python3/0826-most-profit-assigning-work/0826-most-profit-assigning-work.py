class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        #difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
        hm = {}
        for i in range(len(difficulty)):
            if difficulty[i] in hm:
                if hm[difficulty[i]] > profit[i]:
                    continue
            hm[difficulty[i]] = profit[i]
        
        difficulty.sort()

        maxxy = 0

        for num in difficulty:
            maxxy = max(hm[num], maxxy)
            hm[num] = maxxy

        res = 0

        for i in range(len(worker)):
            idx = bisect_left(difficulty, worker[i])
            if idx == len(difficulty):
                idx -= 1
            elif worker[i] != difficulty[idx]:
                idx -= 1
                if idx == -1:
                    continue
            res += hm[difficulty[idx]]
        
        return res