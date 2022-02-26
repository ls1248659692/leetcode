import heapq


# [973] https://leetcode.com/problems/k-closest-points-to-origin/
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
#
# use nsmallest
def kClosest1(points: 'List[List[int]]', K: int) -> 'List[List[int]]':
    return heapq.nsmallest(K, points, key=lambda x: x[0] * x[0] + x[1] * x[1])


# [973] https://leetcode.com/problems/k-closest-points-to-origin/
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
#
# use heappushpop
def kClosest(points: 'List[List[int]]', K: int) -> 'List[List[int]]':
    heap = [(-p[0] * p[0] - p[1] * p[1], p) for p in points[:K]]
    heapq.heapify(heap)

    for p in points[K:]:
        heapq.heappushpop(heap, (-p[0] * p[0] - p[1] * p[1], p))
    return [h[1] for h in heap]


# [313] https://leetcode.com/problems/super-ugly-number/
# Write a program to find the nth super ugly number.
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
#
# generators on a heap, use merge
def nthSuperUglyNumber(self, n, primes):
    uglies = [1]

    def gen(prime):
        for ugly in uglies:
            yield ugly * prime

    merged = heapq.merge(*map(gen, primes))
    while len(uglies) < n:
        ugly = next(merged)
        if ugly != uglies[-1]:
            uglies.append(ugly)
    return uglies[-1]


# [23] https://leetcode.com/problems/merge-k-sorted-lists/
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# use merge
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists):
    # create a generator
    def gen(node):
        while node:
            yield node.val, node
            node = node.next

    dummy = last = ListNode(None)
    for _, last.next in heapq.merge(*map(gen, lists), key=lambda x: x[0]):
        last = last.next
    return dummy.next


# [23] https://leetcode.com/problems/merge-k-sorted-lists/
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# use push and pop
def mergeKLists2(lists):
    # should use wrapper class to override __lt__
    class Wrapper:
        def __init__(self, node):
            self.node = node

        def __lt__(self, other):
            return self.node.val < other.node.val

    head = point = ListNode(0)
    q = []
    for l in lists:
        if l:
            heapq.heappush(q, Wrapper(l))
    while q:
        node = q[0].node
        point.next = node
        point = point.next
        node = node.next
        if node:
            # fast version than pop & push
            heapq.heapreplace(q, Wrapper(node))
        else:
            heapq.heappop(q)
    return head.next


# [855] https://leetcode.com/problems/exam-room/
# Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what
# seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.
class ExamRoom:
    def dist(self, x, y):  # length of the interval (x, y)
        if x == -1:  # note here we negate the value to make it maxheap
            return -y
        elif y == self.N:
            return -(self.N - 1 - x)
        else:
            return -(abs(x - y) // 2)

    def __init__(self, N):
        self.N = N
        self.pq = [(self.dist(-1, N), -1, N)]  # initialize heap

    def seat(self):
        _, x, y = heapq.heappop(self.pq)  # current max interval
        if x == -1:
            seat = 0
        elif y == self.N:
            seat = self.N - 1
        else:
            seat = (x + y) // 2
        heapq.heappush(self.pq, (self.dist(x, seat), x, seat))  # push two intervals by breaking at seat
        heapq.heappush(self.pq, (self.dist(seat, y), seat, y))
        return seat

    def leave(self, p):
        head = tail = None
        for interval in self.pq:  # interval is in the form of (d, x, y)
            if interval[1] == p:
                tail = interval
            if interval[2] == p:
                head = interval
            if head and tail:
                break
        self.pq.remove(head)
        self.pq.remove(tail)
        heapq.heapify(self.pq)  # important! re-heapify after deletion
        heapq.heappush(self.pq, (self.dist(head[1], tail[2]), head[1], tail[2]))


# [857] https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
# There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].
# Return the least amount of money needed to form a paid group satisfying the above conditions.
def mincostToHireWorkers(quality, wage, K):
    workers = sorted((w / q, q) for w, q in zip(wage, quality))
    qsum, heap, res = 0, [], float('inf')
    for r, q in workers:
        heapq.heappush(heap, -q)
        qsum += q
        if len(heap) > K: qsum += heapq.heappop(heap)
        if len(heap) == K: res = min(res, qsum * r)
    return res
