import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            a = -heapq.heappop(heap)  # largest element
            b = -heapq.heappop(heap)  # second largest element

            if a != b:
                heapq.heappush(heap, -(a - b))

        return -heap[0] if heap else 0