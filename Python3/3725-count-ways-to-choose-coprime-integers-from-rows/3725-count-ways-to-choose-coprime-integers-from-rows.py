from itertools import combinations

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149]
        mod = 10**9 + 7
        m = len(mat)
        n = len(mat[0])
        total = pow(n, m, mod)
        for p in primes:
            count = 1
            for row in mat:
                count *= len([x for x in row if x % p == 0])
                count %= mod
            total -= count
            total %= mod
        for p1, p2 in combinations(primes, 2):
            q = p1 * p2
            if q > 150:
                continue
            count = 1
            for row in mat:
                count *= len([x for x in row if x % q == 0])
                count %= mod
            total += count
            total %= mod
        for p1, p2, p3 in combinations(primes, 3):
            q = p1 * p2 * p3
            if q > 150:
                continue
            count = 1
            for row in mat:
                count *= len([x for x in row if x % q == 0])
                count %= mod
            total -= count
            total %= mod
        result = total % mod
        return result