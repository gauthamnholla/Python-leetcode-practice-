class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], 
                                   w: int, m: int) -> int:

        mx, ans = max(arrivals), 0
        ctr = [0] * (mx + 1)
      
        for idx, rght in enumerate(arrivals):
            if idx >= w: 
                left = arrivals[idx - w]
                ctr[left]-= (left != 0)

            if ctr[rght] == m:
                ans+= 1
                arrivals[idx] = 0
            else:
                ctr[rght]+= 1
                
        return ans