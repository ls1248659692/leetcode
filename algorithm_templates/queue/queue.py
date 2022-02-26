# queue common operation: push, pop, top
# queue is widely used in BFS
# FIFO: First In, First Out
#
# Time:  O(1)
# Space: O(n)
from collections import deque


def queue_operations():
    # initialization
    queue = deque()

    # size of queue
    size = len(queue)

    # push (into back)
    queue.append(1)

    # head
    head = queue[0]

    # tail
    tail = queue[-1]

    # pop (from front)
    queue.popleft()

    '''
    for double-ended queue
    '''
    # push into front
    queue.appendleft(1)

    # pop from back
    queue.pop()