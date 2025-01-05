import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        # Heapify the nums array
        heapq.heapify(self.heap)

        # if the heap has more than k element, remove them
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        """
        Add a new number to the stream and return the k-th largest element.

        Returns:
        int: The k-th largest element in the stream.
        """
        # Push the new value into the min-heap
        heapq.heappush(self.heap, val)

        # If the heap exceeds size k, remove the smallest element (heap root)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # The root of the heap is now the k-th largest element
        return self.heap[0]
