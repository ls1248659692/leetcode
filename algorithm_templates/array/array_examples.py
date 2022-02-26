from functools import reduce
from collections import Counter


# [852] https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
#
# linear search
def peakIndexInMountainArray1(A):
    for i in range(len(A)):
        if A[i] > A[i + 1]:
            return i


# binary search
def peakIndexInMountainArray2(A):
    lo, hi = 0, len(A)
    while lo < hi:
        mi = (lo + hi) // 2
        if A[mi] < A[mi + 1]:
            lo = mi + 1
        else:
            hi = mi
    return lo


# [220] https://leetcode.com/problems/contains-duplicate-iii/
# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the
# absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
#
# bucket sort solution
# suppose we have consecutive buckets covering the range of nums with each bucket a width of (t+1).
# if there are two item with difference <= t, one of the two will happen:
# (1) the two in the same bucket
# (2) the two in neighbor buckets
def containsNearbyAlmostDuplicate(nums: 'List[int]', k: int, t: int) -> bool:
    if t < 0: return False
    lookup = {}
    for i in range(len(nums)):
        b_idx = nums[i] // (t + 1)
        if b_idx in lookup:
            return True
        if b_idx - 1 in lookup and abs(nums[i] - lookup[b_idx - 1]) < t + 1:
            return True
        if b_idx + 1 in lookup and abs(nums[i] - lookup[b_idx + 1]) < t + 1:
            return True
        lookup[b_idx] = nums[i]
        if i >= k: del lookup[nums[i - k] // (t + 1)]
    return False


# [31] https://leetcode.com/problems/next-permutation/
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
def nextPermutation(nums: 'List[int]') -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n <= 1:
        return

    def reverse_inplace(i, j):
        left, right = i, j - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    for i in range(1, n)[::-1]:
        if nums[i - 1] < nums[i]:
            break
    else:
        reverse_inplace(0, n)
        return

    for j in range(i, n)[::-1]:
        if nums[j] > nums[i - 1]:
            nums[j], nums[i - 1] = nums[i - 1], nums[j]
            break

    reverse_inplace(i, n)


# [41] https://leetcode.com/problems/first-missing-positive/
# Given an unsorted integer array, find the smallest missing positive integer.
def firstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        # replace iteratively until all in place
        while 0 < nums[i] < n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i, num in enumerate(nums):
        if i != num - 1:
            return i + 1
    return n + 1


# [280] https://leetcode.com/problems/wiggle-sort/
# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]...
def wiggleSort1(nums: 'List[int]') -> None:
    for i in range(len(nums) - 1):
        if i % 2 == (nums[i] < nums[i + 1]):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]


def wiggleSort2(nums):
    # neat, brilliant and beautiful trick
    for i in range(len(nums)):
        nums[i:i + 2] = sorted(nums[i:i + 2], reverse=i % 2)


# [245] https://leetcode.com/problems/shortest-word-distance-iii/
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
# word1 and word2 may be the same and they represent two individual words in the list.
def shortestWordDistance(words: 'List[str]', word1: str, word2: str) -> int:
    # cur_word represents both word1 and word2, elegant here
    cur_word, idx, min_dist = None, 0, len(words)
    for i, w in enumerate(words):
        if w not in (word1, word2):
            continue
        if cur_word and (word1 == word2 or w != cur_word):
            min_dist = min(min_dist, i - idx)
        cur_word, idx = w, i
    return min_dist


# [238] https://leetcode.com/problems/product-of-array-except-self/
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the
# product of all the elements of nums except nums[i].
def productExceptSelf(nums: 'List[int]') -> 'List[int]':
    n = len(nums)
    res, product = [0] * n, 1
    for i in range(n):
        res[i] = product
        product *= nums[i]
    product = 1
    for i in range(n)[::-1]:
        res[i] *= product
        product *= nums[i]
    return res


# [448] https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Find all the elements of [1, n] inclusive that do not appear in this array.
def findDisappearedNumbers(nums: 'List[int]') -> 'List[int]':
    for i in range(len(nums)):
        # replace iteratively utils all in right places
        while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    return [i + 1 for i, num in enumerate(nums) if num != i + 1]


# [277] https://leetcode.com/problems/find-the-celebrity/
# Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
def findCelebrity(n):
    # fake api
    def knows(a, b):
        return True

    candidate = 0
    # if there is a celebrity, he/she must be the "maximum" of the n people
    # find the only one who is a candidate possibly
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i

    # the relation after candidate has been checked in previous loop
    for i in range(candidate):
        if knows(candidate, i):
            return -1

    for i in range(n):
        if not knows(i, candidate):
            return -1

    return candidate


# [845] https://leetcode.com/problems/longest-mountain-in-array/
# Given an array A of integers, return the length of the longest mountain.
# one pass
def longestMountain1(A):
    res = up = down = 0
    for i in range(1, len(A)):
        if down and A[i - 1] < A[i] or A[i - 1] == A[i]: up = down = 0
        up += A[i - 1] < A[i]
        down += A[i - 1] > A[i]
        if up and down: res = max(res, up + down + 1)
    return res


# two-pass
def longestMountain2(A):
    up, down = [0] * len(A), [0] * len(A)
    for i in range(1, len(A)):
        if A[i] > A[i - 1]: up[i] = up[i - 1] + 1
    for i in range(len(A) - 1)[::-1]:
        if A[i] > A[i + 1]: down[i] = down[i + 1] + 1
    return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])


# [853] https://leetcode.com/problems/car-fleet/
# How many car fleets will arrive at the destination?
def carFleet(target, position, speed):
    time = [(target - p) / s for p, s in sorted(zip(position, speed))]
    res = cur = 0
    for t in time[::-1]:
        if t > cur:
            res += 1
            cur = t
    return res


# [77] https://leetcode.com/problems/combinations/
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# recursively
def combine1(n: 'int', k: 'int') -> 'List[List[int]]':
    if k == 0:
        return [[]]

    # add last element
    return [pre + [i] for i in range(k, n + 1) for pre in combine1(i - 1, k - 1)]


# iteratively
def combine2(n: 'int', k: 'int') -> 'List[List[int]]':
    res = [[]]
    for _ in range(k):
        # from large to small, add last element, the last element is range of [1, pre)
        res = [[i] + c for c in res for i in range(1, c[0] if c else n + 1)]
    return res


# reduce
def combine3(n: 'int', k: 'int') -> 'List[List[int]]':
    res = [[]]
    for _ in range(k):
        res = reduce(lambda x, y: x + [[i] + y for i in range(1, y[0] if y else n + 1)], res, [])
    return res


# [229] https://leetcode.com/problems/majority-element-ii/
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
# use Counter
def majorityElement1(nums):
    ctr = Counter()
    for n in nums:
        ctr[n] += 1
        if len(ctr) == 3:
            # Counter - operator
            ctr -= Counter(set(ctr))
    return [n for n in ctr if nums.count(n) > len(nums) // 3]


# Boyer-Moore Majority Vote algorithm
def majorityElement2(nums: 'List[int]') -> 'List[int]':
    if not nums:
        return []
    cand1, cand2, count1, count2 = 0, 1, 0, 0
    for n in nums:
        if n == cand1:
            count1 += 1
        elif n == cand2:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = n, 1
        elif count2 == 0:
            cand2, count2 = n, 1
        else:
            count1 -= 1
            count2 -= 1
    return [n for n in [cand1, cand2] if nums.count(n) > len(nums) // 3]
