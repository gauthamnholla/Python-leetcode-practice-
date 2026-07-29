import numpy as np

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        
        # Start with the first row as our initial 'K-Smallest Field'
        # We only ever need to keep the smallest k elements
        res = np.array(mat[0][:k])
        
        for i in range(1, m):
            # 1. Broad-cast current results against the next row
            # res[:, None] creates a column, mat[i][None, :k] creates a row
            # The result is a (len(res), k) matrix of all possible sums
            next_row = np.array(mat[i][:k])
            
            # The 'Implicit Field' of all pairwise sums between current res and next_row
            field = res[:, np.newaxis] + next_row
            
            # 2. Flatten and find the top K
            # We use partition instead of sort because we only need the smallest k
            flat_field = field.ravel()
            if len(flat_field) > k:
                # np.partition is O(N), much faster than O(N log N) sorting
                indices = np.argpartition(flat_field, k - 1)[:k]
                res = np.sort(flat_field[indices])
            else:
                res = np.sort(flat_field)
                
        return int(res[k-1])