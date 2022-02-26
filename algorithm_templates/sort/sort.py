# all kinds of sort algorithm, just some common versions to show its idea.
# here I unify the api as xxx_sort(arr), changed in-place
#
# currently include:
# quick, merge, insert, bubble, selection, heap, shell, bucket, counting, radix, topological
#
# constant space vs extra space (merge O(n), counting O(k), bucket O(n+k), radix O(n+k))
#
# in place vs out place (merge, counting, bucket, radix)
#
# stable vs unstable (selection, quick, heap, shell)
#
# comparison based vs non-comparison based (radix, bucket, counting)
#
# comparison of counting, bucket and radix sort: all use bucket idea
# counting sort:  store the single key in bucket
# bucket sort:    store a range in bucket
# radix sort:     store each part of element in bucket

# sort      average     best        worst       space   place       stable      comparison
# bubble    O(n^2)      O(n)        O(n^2)      O(1)    in-place    stable      comparison
# selection O(n^2)      O(n^2)      O(n^2)      O(1)    in-place    unstable    comparison
# insert    O(n^2)      O(n)        O(n^2)      O(1)    in-place    stable      comparison
# shell     O(nlogn)    O(nlogn^2)  O(nlogn^2)  O(1)    in-place    unstable    comparison
# merge     O(nlogn)    O(nlogn)    O(nlogn)    O(n)    out-place   stable      comparison
# quick     O(nlogn)    O(nlogn)    O(n^2)      O(logn) in-place    unstable    comparison
# heap      O(nlogn)    O(nlogn)    O(nlogn)    O(1)    in-place    unstable    comparison
# counting  O(n+k)      O(n+k)      O(n+k)      O(k)    out-place   stable      non-comparison
# bucket    O(n+k)      O(n+k)      O(n^2)      O(n+k)  out-place   stable      non-comparison
# radix     O(nk)       O(nk)       O(nk)       O(n+k)  out-place   stable      non-comparison

import random
import time
from collections import deque
from collections import defaultdict

'''
quick sort 
avg: O(nlogn), best: O(nlogn), worst: O(n^2), space: O(logn), in-place, unstable, comparison
fastest in large-scale and out-of-order data, divide & conquer
'''


def quick_sort(arr):
    quick_sort_rec(arr, 0, len(arr) - 1)


# hi is included, in range [lo, hi]
def quick_sort_rec(arr, lo, hi):
    if lo < hi:
        pivot = partition(arr, lo, hi)

        quick_sort_rec(arr, lo, pivot - 1)
        quick_sort_rec(arr, pivot + 1, hi)


def partition(arr, lo, hi):
    # choose pivot by median-of-three
    x, idx = sorted(((arr[lo], lo), (arr[hi], hi), (arr[lo + hi >> 1], lo + hi >> 1)))[1]
    arr[lo], arr[idx] = arr[idx], arr[lo]
    while lo < hi:
        while lo < hi and arr[hi] >= x:
            hi -= 1
        arr[lo] = arr[hi]
        while lo < hi and arr[lo] <= x:
            lo += 1
        arr[hi] = arr[lo]
    arr[lo] = x
    return lo


'''
merge sort
avg: O(nlogn), best: O(nlogn), worst: O(nlogn), space: O(n), out-place, stable, comparison
divide & conquer
'''


# the version with a fixed temp array
def merge_sort(arr):
    merge_sort_rec(arr, 0, len(arr) - 1, [0] * len(arr))


def merge_sort_rec(arr, first, last, temp):
    if first < last:
        mid = (first + last) // 2
        merge_sort_rec(arr, first, mid, temp)
        merge_sort_rec(arr, mid + 1, last, temp)
        merge(arr, first, mid, last, temp)


def merge(arr, first, mid, last, temp):
    i, j = first, mid + 1
    m, n = mid, last
    k = 0
    while i <= m and j <= n:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= m:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= n:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(k):
        arr[first + i] = temp[i]


def merge_sort2(arr):
    res = merge_sort_rec2(arr)
    for i in range(len(arr)):
        arr[i] = res[i]


def merge_sort_rec2(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_rec2(arr[:mid])
    right = merge_sort_rec2(arr[mid:])
    return merge1(left, right)


def merge1(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res


# more pythonic but slower
def merge2(left, right):
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    return res + (left or right)


# slowest
def merge3(left, right):
    res = []
    while left and right:
        if left[-1] > right[-1]:
            res.insert(0, left.pop())
        else:
            res.insert(0, right.pop())
    return (left or right) + res


'''
insert sort
avg: O(n^2), best: O(n), worst: O(n^2), space: O(1), in-place, stable, comparison
fast in small-scale and almost sorted data 
'''


def insert_sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = x


'''
bubble sort
avg: O(n^2), best:O(n), worst: O(n^2), space:O(1), in-place, stable, comparison
optimization: 
1. flag whether swap last round, if not, end sort
2. flag the last swap place, [last_swap, j] has been sorted, just skip it.
'''


# bubble the max to right most
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# optimization
def bubble_sort2(arr):
    i = len(arr) - 1
    while i > 0:
        last_swap = 0
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                last_swap = j
        # if last_swap=0, it means no swap in last round, end sort
        # [last_swap, i] has been sorted, start from last_swap
        i = last_swap


'''
selection sort
avg: O(n^2), best: O(n^2), worst: O(n^2), space: O(1), in-place, unstable, comparison
most stable in time cost, always O(n^2), and easy understanding, used in small scale data
'''


def selection_sort(arr):
    for i in range(len(arr)):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]


'''
heap sort
avg: O(nlogn), best: O(nlogn), worst: O(nlogn), space: O(1), in-place, unstable, comparison
not only a sort algorithm, this structure (priority queue) can do more thing.
'''


def heap_sort(arr):
    # build max heap
    for i in range(len(arr) // 2)[::-1]:
        heap_adjust(arr, i, len(arr))

    # adjust from last element
    for i in range(1, len(arr))[::-1]:
        # swap first with the last, make the right most is maximum
        arr[0], arr[i] = arr[i], arr[0]
        heap_adjust(arr, 0, i)


def heap_adjust(arr, i, n):
    cur = arr[i]
    while 2 * i + 1 < n:
        # get child index in heap
        child = 2 * i + 1

        # choose the larger child
        if child < n - 1 and arr[child + 1] > arr[child]:
            child += 1

        # if child is larger than parent, sift up
        if cur < arr[child]:
            arr[i], arr[child] = arr[child], cur
            i = child
        else:
            break


'''
shell sort
avg: O(nlogn), best: O(nlogn^2), worst: O(nlogn^2), space: O(1), in-place, unstable, comparison
improvement of insertion sort
'''


def shell_sort(arr):
    # Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1.
    gap = len(arr) // 2
    # loop over the gaps
    while gap > 0:
        # do the insertion sort
        for i in range(gap, len(arr)):
            val = arr[i]
            j = i
            while j >= gap and arr[j - gap] > val:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = val
        gap //= 2


'''
counting sort
avg: O(n+k), best:O(n+k), worst:O(n+k), space:O(k), out-place, stable, non-comparison
relatively concentrated values
'''


def counting_sort(arr):
    min_val, max_val = min(arr), max(arr)
    size = max_val - min_val + 1
    counter = [0] * size

    for i in range(len(arr)):
        counter[arr[i] - min_val] += 1

    idx = 0
    for i, v in enumerate(counter):
        # use slice assignment
        arr[idx:idx + v] = [i + min_val] * v
        idx += v


'''
bucket sort
avg: O(n+k), best:O(n+k), worst:O(n^2), space:O(n+k), out-place, stable, non-comparison
improvement of counting sort, usually used with hash 
'''
DEFAULT_BUCKET_SIZE = 5


def bucket_sort(arr, size=DEFAULT_BUCKET_SIZE):
    min_val, max_val = min(arr), max(arr)

    # initialize buckets
    count = (max_val - min_val) // size + 1
    buckets = [[] for _ in range(count)]

    # put values in buckets
    for i in range(len(arr)):
        buckets[(arr[i] - min_val) // size].append(arr[i])

    # sort buckets and place back into input array
    i = 0
    for bucket in buckets:
        insert_sort(bucket)
        # use slice assignment
        arr[i:i + len(bucket)] = bucket
        i += len(bucket)


# with hash
def bucket_sort2(arr):
    # get hash codes
    code = hashing(arr)
    buckets = [[] for _ in range(code[1])]
    # distribute data into buckets: O(n)
    for i in arr:
        x = re_hashing(i, code)
        buckets[x].append(i)

    i = 0
    # merge the buckets: O(n)
    for bucket in buckets:
        insert_sort(bucket)
        arr[i:i + len(bucket)] = bucket
        i += len(bucket)


def hashing(arr):
    return [max(arr), int(len(arr) ** 0.5)]


def re_hashing(i, code):
    return int(i / code[0] * (code[1] - 1))


'''
radix sort
avg: O(nk), best:O(nk), worst:O(nk), space:O(n+k), out-place, stable, non-comparison
improvement of counting sort
'''


def radix_sort(arr):
    radix = 10
    max_length = False
    placement = 1

    while not max_length:
        max_length = True
        # declare and initialize buckets
        buckets = [[] for _ in range(radix)]

        # split arr between lists
        for i in arr:
            temp = i // placement
            buckets[temp % radix].append(i)
            if max_length and temp > 0:
                max_length = False

        # assign from bucket to arr
        i = 0
        for bucket in buckets:
            insert_sort(bucket)
            # use slice assignment
            arr[i:i + len(bucket)] = bucket
            i += len(bucket)

        # move to next digit
        placement *= radix
    return arr


'''
topological sort
in a directed graph, a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, 
u comes before v in the ordering. 
'''

GRAY, BLACK = 0, 1


def topological_sort(graph):
    order, enter, state = deque(), set(graph), {}

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY:
                raise ValueError("cycle")
            if sk == BLACK:
                continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter:
        dfs(enter.pop())
    return order


if __name__ == '__main__':
    def sort_test(sort_func):
        start = time.time()
        for _ in range(100):
            nums = [random.randrange(1, 250) for _ in range(1000)]
            nums1 = sorted(nums)
            sort_func(nums)
            if nums1 != nums:
                print('incorrect', )
        end = time.time()
        print('{:15s} time: {}'.format(sort_func.__name__, end - start))


    sort_test(quick_sort)
    sort_test(merge_sort)
    sort_test(merge_sort2)
    sort_test(heap_sort)
    sort_test(shell_sort)
    sort_test(counting_sort)
    sort_test(bucket_sort)
    sort_test(bucket_sort2)
    sort_test(radix_sort)

    # put turtle algorithms to the tail
    sort_test(insert_sort)
    sort_test(bubble_sort)
    sort_test(bubble_sort2)
    sort_test(selection_sort)

    graph = defaultdict(list)
    graph['A'].append('B')
    graph['B'].append('D')
    graph['C'].append('A')
    print(topological_sort(graph))
