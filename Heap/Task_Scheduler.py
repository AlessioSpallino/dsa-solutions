import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # Counter provides me with a frequency Object
        # I could also build it looping through all tasks
        frequency = Counter(tasks)

        # Create a maxHeap
        heap = []
        for i,v in frequency.items():
            heapq.heappush(heap, (-v, i)) # E.g., (-2, "A")

        #initialize a cooldown queue
        cooldown = deque()
        result = 0

        while heap or cooldown:
            result+=1

            if heap:
                # execute task
                task = heapq.heappop(heap)
                freq = task[0]
                value = task[1]
                # --------------

                if freq + 1 < 0:
                    # (cooldownTime, remainingFreq, taskName)
                    cooldown.append((result + n, freq + 1, value))

            if cooldown and cooldown[0][0] == result:
                _, freq, name = cooldown.popleft()
                heapq.heappush(heap, (freq, name))

        return result
