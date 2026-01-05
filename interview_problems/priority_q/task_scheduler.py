from collections import deque, Counter
import heapq
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass(order=True)
class IntervalTask:
    frequency: int
    label: str=field(compare=False)

@dataclass
class IdleTaskFuture:
    expected_clock: int
    label: str

class Solution:
    def check_dict_queue_empty(self, dict_to_queue: Dict) -> bool:
        for key, value in dict_to_queue.items():
            if len(value) > 0:
                return False
        return True


    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
