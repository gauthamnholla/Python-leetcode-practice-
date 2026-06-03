class Solution:
    def minCost(self, arr: List[int], 
                      brr: List[int], k: int) -> int:
        
        def score(a_list: List[int], b_list: List[int]):

            res = 0
            for a, b in zip (a_list, b_list):
                res+= abs(a - b)

            return res    


        return min(score(arr, brr) , 
                   score(sorted(arr), sorted(brr)) + k)