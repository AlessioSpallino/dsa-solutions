import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        # Create a maxHeap in this scenario
        for stone in stones:
            heapq.heappush(heap, -stone)

        while(len(heap) > 1):
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, -(x-y))

        # If the heap is not empty, return the last stone's weight; otherwise, return 0
        return -heap[0] if heap else 0
