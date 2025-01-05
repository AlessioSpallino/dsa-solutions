import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap of size k
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            # Maintain the heap size at most k
            if len(heap) > k:
                heapq.heappop(heap)

        # The root of the heap is the k-th largest element
        return heap[0]
