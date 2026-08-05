class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        heap = []
        n = len(arr)

        for i in range(0,n):
            for j in range(i+1,n):
                fact = (arr[i]/arr[j],[arr[i],arr[j]])
                heapq.heappush(heap,fact)

        ans = -1

        for _ in range(k):
            ans = heapq.heappop(heap)


        return ans[1]