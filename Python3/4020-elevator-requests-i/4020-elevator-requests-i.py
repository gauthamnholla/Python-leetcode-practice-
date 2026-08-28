
class Solution:
    def elevatorRequests(self, n, requests):
        m = len(requests)
        total = 0

        for i in range(1, m):
            total += abs(requests[i - 1] - requests[i])

        return total + requests[0]