class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # given an array of CPU tasks `tasks` (list of strings)
        # where tasks[i] is an uppercase english character from A to Z
        # you are also given an integer N

        # each cpu cycle allows the completion of a single task, and tasks may be completed in any order
        # the only constraint is that identical tasks must be separated by at least `n` cpu cycles
        # to cooldown the cpu

        # return the minimum number of CPU cycles required to complete all the tasks

        freqMap = {} # char : freq
        for task in tasks:
            freqMap[task] = freqMap.get(task,0) - 1
        
        maxHeap = list(freqMap.values())
        heapq.heapify(maxHeap)
        queue = [] # (itemcount, waittime)
        cycles = 0

        while maxHeap or queue:
            if queue and (cycles >= queue[0][1]):
                heapq.heappush(maxHeap,queue.pop(0)[0]) # take off queue, back to heap

            if maxHeap:
                leftCount = heapq.heappop(maxHeap)+1
                if leftCount < 0:
                    queue.append((leftCount,cycles + n + 1))
                cycles += 1
            else:
                # wait until top of queue is done
                cycles = queue[0][1]

            
        return cycles

        



        