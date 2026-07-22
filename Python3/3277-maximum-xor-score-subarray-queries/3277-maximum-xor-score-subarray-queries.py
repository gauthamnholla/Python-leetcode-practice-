class Solution:
    def maximumSubarrayXor(self, A: List[int], queries: List[List[int]]) -> List[int]:
        B = [A]
        while len(B[-1]) != 1:
            B.append([B[-1][i] ^ B[-1][i+1] for i in range(len(B[-1]) - 1)])
        
        for i in range(1, len(B)):
            for j in range(len(B[i])):
                B[i][j] = max(B[i][j], B[i-1][j], B[i-1][j+1])
        
        return [B[r-l][l] for l, r in queries]        