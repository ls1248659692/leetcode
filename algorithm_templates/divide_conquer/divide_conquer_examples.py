import random


# [50] https://leetcode.com/problems/powx-n
# Implement pow(x, n), which calculates x raised to the power n
def myPow(self, x, n):
    if not n:
        return 1
    if n < 0:
        return 1 / self.myPow(x, -n)
    if n % 2:
        return x * self.myPow(x, n - 1)
    return self.myPow(x * x, n / 2)


# [169] https://leetcode.com/problems/majority-element/
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊n/2⌋ times.
def majorityElement(nums):
    def majority_element_rec(lo, hi):
        # base case; the only element in an array of size 1 is the majority
        # element.
        if lo == hi:
            return nums[lo]

        # recurse on left and right halves of this slice.
        mid = lo + (hi - lo) // 2
        left = majority_element_rec(lo, mid)
        right = majority_element_rec(mid + 1, hi)

        # if the two halves agree on the majority element, return it.
        if left == right:
            return left

        # otherwise, count each element and return the "winner".
        # seems inefficient here
        left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

        return left if left_count > right_count else right

    return majority_element_rec(0, len(nums) - 1)


# [53] https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the contiguous sub-array which has the largest sum and return its sum.
def maxSubArray(nums):
    def maximum_sub_array_sum_rec(nums):
        if not nums:
            return [float("-inf"), float("-inf"), float("-inf"), 0]
        mid = len(nums) // 2
        mid_num = nums[mid]
        left_max1, right_max1, all_max1, total1 = maximum_sub_array_sum_rec(nums[:mid])
        left_max2, right_max2, all_max2, total2 = maximum_sub_array_sum_rec(nums[mid + 1:])

        total = total1 + total2 + mid_num
        left_max = max(left_max1, total1 + mid_num + left_max2, total1 + mid_num)
        right_max = max(right_max2, total2 + mid_num, total2 + mid_num + right_max1)
        all_max = max(all_max1, all_max2, mid_num, mid_num + right_max1, mid_num + left_max2,
                      mid_num + right_max1 + left_max2)
        return left_max, right_max, all_max, total

    return maximum_sub_array_sum_rec(nums)[2]


# [973] https://leetcode.com/problems/k-closest-points-to-origin/
# Find the K closest points to the origin (0, 0)
#
# partition and sort, similar to quick sort
def kClosest(points, K):
    dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2

    def sort(i, j, K):
        # Partially sorts A[i:j+1] so the first K elements are
        # the smallest K elements.
        if i >= j: return

        # Put random element as A[i] - this is the pivot
        k = random.randint(i, j)
        points[i], points[k] = points[k], points[i]

        mid = partition(i, j)
        if K < mid - i + 1:
            sort(i, mid - 1, K)
        elif K > mid - i + 1:
            sort(mid + 1, j, K - (mid - i + 1))

    def partition(i, j):
        # Partition by pivot A[i], returning an index mid
        # such that A[i] <= A[mid] <= A[j] for i < mid < j.
        oi = i
        pivot = dist(i)
        i += 1

        while True:
            while i < j and dist(i) < pivot:
                i += 1
            while i <= j and dist(j) >= pivot:
                j -= 1
            if i >= j: break
            points[i], points[j] = points[j], points[i]

        points[oi], points[j] = points[j], points[oi]
        return j

    sort(0, len(points) - 1, K)
    return points[:K]


# [4] https://leetcode.com/problems/median-of-two-sorted-arrays/
# Find the median of the two sorted arrays
def medianSortedArrays(a, b):
    def select(s, k):
        pivot = s[len(s) // 2]
        sl, sp, sr = [], [], []
        for i in s:
            if i < pivot:
                sl.append(i)
            elif i == pivot:
                sp.append(i)
            else:
                sr.append(i)
        if k <= len(sl):
            return select(sl, k)
        elif len(sl) < k <= len(sl) + len(sp):
            return pivot
        elif k > len(sl) + len(sp):
            return select(sr, k - len(sl) - len(sp))

    c = a + b
    length = len(c)
    odd_median = select(c, 1 + length // 2)
    if length % 2 != 0:
        return odd_median
    even_median = select(c, length // 2)
    return (odd_median + even_median) / 2


# [23] https://leetcode.com/problems/merge-k-sorted-lists/
# Merge k sorted linked lists and return it as one sorted list
def mergeKLists(lists):
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def merge2Lists(l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next

    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = merge2Lists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else lists
