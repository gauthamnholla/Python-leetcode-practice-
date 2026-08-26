import sys

# Increase recursion depth for deep "Legacy" trees
sys.setrecursionlimit(200000)

class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        # A tree with E edges always has E + 1 nodes.
        n = len(edges) + 1 
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 1. Domain Mapping: Hash the guesses into a single "Source of Truth"
        # We use a set of tuples for O(1) membership testing.
        guess_set = set((u, v) for u, v in guesses)
            
        # 2. First Pass: Base Case (Root 0)
        # Iterative DFS to avoid recursion overhead for the initial count.
        correct_at_root_0 = 0
        stack = [(0, -1)]
        while stack:
            u, p = stack.pop()
            for v in adj[u]:
                if v != p:
                    if (u, v) in guess_set:
                        correct_at_root_0 += 1
                    stack.append((v, u))
        
        # 3. Second Pass: The Re-rooting Calculus
        self.valid_roots = 0
        
        def dfs_reroot(u, p, current_score):
            # Check the threshold: Is this node a safe root?
            if current_score >= k:
                self.valid_roots += 1
                
            for v in adj[u]:
                if v != p:
                    # Apply the Delta:
                    # When v becomes root, the edge (u, v) flips to (v, u).
                    next_score = current_score
                    if (u, v) in guess_set: next_score -= 1
                    if (v, u) in guess_set: next_score += 1
                    
                    dfs_reroot(v, u, next_score)
        
        dfs_reroot(0, -1, correct_at_root_0)
        return self.valid_roots    