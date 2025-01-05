import math
import heapq

class Solution:
    def distanceToOrigin(self, point: List[int]) -> float:
        oX, oY = 0, 0
        x, y = point[0], point[1]

        return math.sqrt((oX - x)**2 + (oY - y)**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for point in points:
            distance = self.distanceToOrigin(point)
            heapq.heappush(heap, (distance, point)) # E.g., (1, [0,2])

        while(k > 0):
            result.append(heapq.heappop(heap)[1])
            k-=1;
        
        return result
