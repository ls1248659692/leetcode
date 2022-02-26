from collections import defaultdict

'''
old & new state: old, new = new, cur_result
'''


# [198] https://leetcode.com/problems/house-robber/
# determine the maximum amount of money you can rob tonight without adjacent houses
def rob(nums: 'List[int]') -> 'int':
    last, now = 0, 0
    for i in nums:
        last, now = now, max(last + i, now)
    return now


# [21] https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a new list.
#
# first make sure a starts smaller, use its head as result, and merge the remainders behind it.
def mergeTwoLists1(a, b):
    if a and b:
        if a.val > b.val:
            a, b = b, a
        a.next = mergeTwoLists1(a.next, b)
    return a or b


# first make sure that a is the "better" one (meaning b is None or has larger/equal value). Then merge the remainders behind a.
def mergeTwoLists2(a: int, b: int) -> int:
    if not a or b and a.val > b.val:
        a, b = b, a
    if a:
        a.next = mergeTwoLists2(a.next, b)
    return a


# [904] https://leetcode.com/problems/fruit-into-baskets/
# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
# What is the total amount of fruit you can collect with this procedure?
def totalFruit(tree):
    res = cur = count_b = a = b = 0
    for c in tree:
        cur = cur + 1 if c in (a, b) else count_b + 1
        count_b = count_b + 1 if c == b else 1
        if b != c:
            a, b = b, c
        res = max(res, cur)
    return res


# [91] https://leetcode.com/problems/decode-ways/
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
def numDecodings(s: str) -> int:
    if len(s) > 0 and s[0] > '0':
        a, b = 1, 1
    else:
        return 0
    for i in range(1, len(s)):
        if s[i] == '0':
            if s[i - 1] > '2' or s[i - 1] == '0':
                return 0
            a, b = 0, a
        elif s[i - 1] == '1' or (s[i - 1] == '2' and s[i] < '7'):
            a, b = b, a + b
        else:
            a, b = b, b
    return b


'''
slow & fast pointer
'''


# [19] https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Given a linked list, remove the n-th node from the end of list and return its head.
def removeNthFromEnd(head, n):
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    dummy = ListNode(0)
    dummy.next = head
    slow, fast = dummy, dummy

    for i in range(n):
        fast = fast.next

    while fast.next:
        slow, fast = slow.next, fast.next

    slow.next = slow.next.next

    return dummy.next


# [26] https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
def removeDuplicates(nums):
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


'''
left & right boundary or index
'''


# [11] https://leetcode.com/problems/container-with-most-water/
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
def maxArea(height):
    left, right = 0, len(height) - 1
    area_max = (right - left) * min(height[left], height[right])

    while left < right:
        # judge which side decide the area (shorter height)
        if height[left] <= height[right]:
            last_height = height[left]
            while height[left] <= last_height and left < right:  # skip all the height less than current
                left += 1
        else:
            last_height = height[right]
            while height[right] <= last_height and left < right:  # skip all the height less than current
                right -= 1

        if left >= right:
            return area_max
        area_max = max(area_max, (right - left) * min(height[left], height[right]))
    return area_max


# [42] https://leetcode.com/problems/trapping-rain-water/
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
def trap(height):
    if not height:
        return 0
    left, right, result = 0, len(height) - 1, 0
    while left < right:
        if height[left] <= height[right]:
            short_height = height[left]
            left += 1
            while left < right and height[left] <= short_height:
                result += short_height - height[left]
                left += 1
        else:
            short_height = height[right]
            right -= 1
            while left < right and height[right] <= short_height:
                result += short_height - height[right]
                right -= 1
    return result


# [167] https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
def twoSum(numbers: 'List[int]', target: 'int') -> 'List[int]':
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        if numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1
    return [0, 0]


# [18] https://leetcode.com/problems/4sum/
# Find all unique quadruplets in the array which gives the sum of target.
def fourSum(nums: 'List[int]', target: int) -> 'List[int]':
    result, n = [], len(nums)
    if n < 4: return result
    nums = sorted(nums)

    if sum(nums[-4:]) < target:
        return result

    for i in range(n - 3):
        # boundary checker, stop early
        if sum(nums[i:i + 4]) > target:
            break
        # right boundary checker
        if nums[i] + sum(nums[-3:]) < target:
            continue
        # skip same element, but keep the first one
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # simplify the problem to three sum
        target2 = target - nums[i]
        for j in range(i + 1, n - 2):
            if sum(nums[j:j + 3]) > target2 or sum(nums[-3:]) < target2:
                break
            if nums[j] + sum(nums[-2:]) < target2:
                continue
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # simplify the problem to two sum
            target3 = target2 - nums[j]
            left = j + 1
            right = n - 1
            while left < right:
                if nums[left] + nums[right] == target3:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target3:
                    left += 1
                else:
                    right -= 1
    return result


'''
p1 & p2 from two sequences
'''


# [44] https://leetcode.com/problems/wildcard-matching/
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
def isMatch(s, p):
    s_cur, p_cur, match, star = 0, 0, 0, -1

    while s_cur < len(s):
        if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
            s_cur += 1
            p_cur += 1
        elif p_cur < len(p) and p[p_cur] == '*':
            match = s_cur
            star = p_cur
            p_cur += 1
        elif star != -1:
            p_cur = star + 1
            match += 1
            s_cur = match
        else:
            return False
    while p_cur < len(p) and p[p_cur] == '*':
        p_cur += 1

    if p_cur == len(p):
        return True
    else:
        return False


# [244] https://leetcode.com/problems/shortest-word-distance-ii/
# Design a class which receives a list of words in the constructor, and implements a method that takes
# two words word1 and word2 and return the shortest distance between these two words in the list.
class WordDistance:
    def __init__(self, words: 'List[str]'):
        self.locations = defaultdict(list)
        # Prepare a mapping from a word to all it's locations (indices).
        for i, w in enumerate(words):
            self.locations[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        loc1, loc2 = self.locations[word1], self.locations[word2]
        l1, l2 = 0, 0
        min_diff = float("inf")

        # Until the shorter of the two lists is processed
        while l1 < len(loc1) and l2 < len(loc2):
            min_diff = min(min_diff, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
        return min_diff


'''
# start & end sliding window boundary: start-> end->
'''


# [830] https://leetcode.com/problems/positions-of-large-groups/
# Call a group large if it has 3 or more characters.
def largeGroupPositions(S):
    result = []
    start = 0
    for end in range(len(S)):
        if end == len(S) - 1 or S[end] != S[end + 1]:
            if end - start + 1 >= 3:
                result.append([start, end])
            start = end + 1
    return result


# [3] https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s):
    # create a default dict to maintain state
    counter = defaultdict(int)
    count, start, end, res = 0, 0, 0, 0
    while end < len(s):
        counter[s[end]] += 1
        if counter[s[end]] > 1:
            count += 1
        end += 1
        while count > 0:
            counter[s[start]] -= 1
            if counter[s[start]] > 0:
                count -= 1
            start += 1
        res = max(res, end - start)
    return res


'''
three pointers
'''


# [75] https://leetcode.com/problems/sort-colors/
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are
# adjacent, with the colors in the order red, white and blue.
def sortColors(nums):
    red, white, blue = 0, 0, len(nums) - 1

    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
