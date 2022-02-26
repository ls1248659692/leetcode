# heap, also called priority queue
# heap common operations: heapify, top, heappush, heappop, heappushpop, heapreplace, _siftup/_siftdown,
# nlargest/nsmallest, merge
# heapq in Python, there is only min heap, if you want to a max heap, you should reverse the key or implement __lt__.
#
# Time:  O(1) to find, O(log(n)) to push/pop/sift, O(nlog(n)) to heapify, O(n) to merge
# Space: O(n)
#
# from Queue import PriorityQueue is alternative way, which is a thread-safe class
import heapq


def heap_operations():
    heap = [4, 2, 1, 3]

    # heapify
    heapq.heapify(heap)

    # top
    top = heap[0]

    # heappop
    top = heapq.heappop(heap)

    # heappush
    heapq.heappush(heap, 5)

    # heappushpop = push + pop
    heapq.heappushpop(heap, 0)

    # heapreplace = pop + push
    heapq.heapreplace(heap, 0)

    data = [10, 5, 18, 2, 37, 3, 8, 7, 19, 1]
    heapq.heapify(data)
    old, new = 8, 22  # increase the 8 to 22
    i = data.index(old)
    data[i] = new
    # _siftup, from root to leaf, when increase
    heapq._siftup(data, i)

    old, new = 10, 4  # decrease the 10 to 4
    i = data.index(old)
    data[i] = new
    # _siftdown, from leaf to root, when decrease
    heapq._siftdown(data, 0, i)

    # find n largest by queue
    heapq.nlargest(data, 3)

    # find n smallest by queue
    heapq.nsmallest(data, 3)

    # Merge multiple sorted inputs into a single sorted output
    # e.g. merge timestamped entries from multiple log files
    heapq.merge([1, 3, 5, 7], [0, 2, 4, 8], [5, 10, 15, 20], [], [25])
