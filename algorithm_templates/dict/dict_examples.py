from collections import defaultdict
from collections import Counter
from operator import eq


# [1] https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
def twoSum(nums, target):
    complement = {}
    for i in range(len(nums)):
        if nums[i] in complement:
            return [complement[nums[i]], i]
        else:
            complement[target - nums[i]] = i


# [266] https://leetcode.com/problems/palindrome-permutation/
# Given a string, determine if a permutation of the string could form a palindrome.
def canPermutePalindrome1(s: str) -> bool:
    return len([count for count in Counter(s).values() if count % 2 == 1]) <= 1


def canPermutePalindrome2(s: str) -> bool:
    return len(list(filter(lambda x: x % 2, Counter(s).values()))) <= 1


def canPermutePalindrome3(s: str) -> bool:
    return sum(1 for _ in filter(lambda x: x % 2, Counter(s).values())) <= 1


def canPermutePalindrome4(s: str) -> bool:
    return sum(v % 2 for v in Counter(s).values()) < 2


# [49] https://leetcode.com/problems/group-anagrams/
# Given an array of strings, group anagrams together.
#
# categorize by sorted string
def groupAnagrams1(strs):
    ans = defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()


# [49] https://leetcode.com/problems/group-anagrams/
# Given an array of strings, group anagrams together.
#
# categorize by count
def groupAnagrams2(strs):
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return list(ans.values())


# [36] https://leetcode.com/problems/valid-sudoku
# Determine if a 9x9 Sudoku board is valid.
def isValidSudoku1(board):
    row_counters = [{} for _ in range(9)]
    col_counters = [{} for _ in range(9)]
    box_counters = [{} for _ in range(9)]

    for r_i, row in enumerate(board):
        for c_i, v in enumerate(row):
            if v.isdigit():
                num = int(v) - 1
                box_i = r_i // 3 * 3 + c_i // 3
                if num not in row_counters[r_i] and num not in col_counters[c_i] \
                        and num not in box_counters[box_i]:
                    row_counters[r_i][num] = 1
                    col_counters[c_i][num] = 1
                    box_counters[box_i][num] = 1
                else:
                    return False
    return True


# [170] https://leetcode.com/problems/two-sum-iii-data-structure-design/
# Design and implement a TwoSum class. It should support the following operations: add and find.
class TwoSum2:
    def __init__(self):
        self.data = {}
        self.sum = set()
        self.max = float('-inf')
        self.min = float('inf')

    def add(self, number):
        if number in self.data:
            self.data[number] += 1
        else:
            self.data[number] = 1
        self.max = max(self.max, number)
        self.min = min(self.min, number)

    def find(self, value):
        if value > 2 * self.max or value < 2 * self.min:
            return False
        if value in self.sum:
            return True
        for k in self.data.keys():
            if (value - k != k and value - k in self.data) or (value - k == k and self.data[k] > 1):
                self.sum.add(value)
                return True
        return False


# [311] https://leetcode.com/problems/sparse-matrix-multiplication/
# Given two sparse matrices A and B, return the result of AB.
def multiply(A, B):
    m, n = len(A), len(B[0])
    a_rows = []
    for rows in A:
        a_rows.append({col: v for col, v in enumerate(rows) if v != 0})

    b_cols = []
    for j in range(n):
        b_cols.append({i: B[i][j] for i in range(len(B)) if B[i][j] != 0})

    res = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k, v in a_rows[i].items():
                if k in b_cols[j]:
                    res[i][j] += v * b_cols[j][k]
    return res


# [325] https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
def maxSubArrayLen(nums, k):
    ans, acc = 0, 0  # answer and the accumulative value of nums
    mp = {0: -1}  # key is acc value, and value is the index
    for i in range(len(nums)):
        acc += nums[i]
        # if already exits in mp, only keep the shortest, that is the first one. it solves duplication problem.
        if acc not in mp:
            mp[acc] = i
        if acc - k in mp:
            ans = max(ans, i - mp[acc - k])
    return ans


# [350] https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Given two arrays, write a function to compute their intersection.
#
# use two Counter intersection
def intersect(nums1, nums2):
    a, b = map(Counter, (nums1, nums2))
    return list((a & b).elements())


# [350] https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Given two arrays, write a function to compute their intersection.
#
# use one Counter
def intersect2(nums1, nums2):
    # choose the smaller list as Counter
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    cnt, res = Counter(nums1), []
    for num in nums2:
        if num in cnt and cnt[num] > 0:
            res.append(num)
            cnt[num] -= 1
    return res


# [560] https://leetcode.com/problems/subarray-sum-equals-k/
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
def subarraySum(nums: 'List[int]', k: 'int') -> 'int':
    count, cur_sum = 0, 0
    mapping = defaultdict(int)
    mapping[0] = 1
    for i in range(len(nums)):
        cur_sum += nums[i]
        if cur_sum - k in mapping:
            count += mapping[cur_sum - k]
        mapping[cur_sum] += 1
    return count


# [359] https://leetcode.com/problems/logger-rate-limiter/
# Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given
# timestamp, otherwise returns false.
class Logger:
    def __init__(self):
        self.mem = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.mem or timestamp >= self.mem[message]:
            self.mem[message] = timestamp + 10
            return True
        return False


# [299] https://leetcode.com/problems/bulls-and-cows/
# Write a function to return a hint according to the secret number and friend's guess,
# use A to indicate the bulls and B to indicate the cows.
def getHint1(secret, guess):
    bulls = sum(map(eq, secret, guess))
    both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
    return '%dA%dB' % (bulls, both - bulls)


# & in counter
def getHint2(secret, guess):
    A = sum(a == b for a, b in zip(secret, guess))
    B = Counter(secret) & Counter(guess)
    return "%dA%dB" % (A, sum(B.values()) - A)


# One Pass solution
def getHint3(secret, guess):
    # use arr instead of dict, but slow than it
    counter = [0] * 10
    bulls, cows = 0, 0
    for i, (s, g) in enumerate(zip(secret, guess)):
        if s == g:
            bulls += 1
        else:
            s_i, g_i = ord(s) - ord('0'), ord(g) - ord('0')
            if counter[s_i] < 0: cows += 1
            if counter[g_i] > 0: cows += 1
            counter[s_i] += 1
            counter[g_i] -= 1

    return f'{bulls}A{cows}B'


# [362] https://leetcode.com/problems/design-hit-counter/
# Design a hit counter which counts the number of hits received in the past 5 minutes.
#
# loop list, dict, bisect, bucket
# depends on the data dense and amount
#
# dict solution
class HitCounter1:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = defaultdict(int)

    def hit(self, timestamp: 'int') -> 'None':
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp in self.hits:
            self.hits[timestamp] += 1
        else:
            self.hits[timestamp] = 1

        # 定时清理
        # past = [ts for ts in self.hits if ts < timestamp - 300]
        # for ts in past:
        #     del self.hits[ts]

    def getHits(self, timestamp: 'int') -> 'int':
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        return sum(self.hits[ts] for ts in range(timestamp, timestamp - 300, -1) if ts > 0)


# [362] https://leetcode.com/problems/design-hit-counter/
# Design a hit counter which counts the number of hits received in the past 5 minutes.
#
# bisect queue
class HitCounter2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timed_counter = [[0, 0]]

    def hit(self, timestamp: 'int') -> 'None':
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.timed_counter[-1][0] == timestamp:
            self.timed_counter[-1][1] += 1
        else:
            prev_count = self.timed_counter[-1][1]
            self.timed_counter.append([timestamp, prev_count + 1])

    def getHits(self, timestamp: 'int') -> 'int':
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        t_begin, t_end = timestamp - 300, timestamp
        c_begin, c_end = self._search(t_begin), self._search(t_end)
        return c_end - c_begin

    def _search(self, ts):
        i, j = 0, len(self.timed_counter),
        k = -1
        while i < j:
            k = (i + j) // 2
            if self.timed_counter[k][0] > ts:
                j = k
            elif self.timed_counter[k][0] < ts:
                i = k + 1
            else:
                break
        else:
            k = i - 1
        if k < 0:
            return 0
        else:
            return self.timed_counter[k][1]


# [362] https://leetcode.com/problems/design-hit-counter/
# Design a hit counter which counts the number of hits received in the past 5 minutes.
#
# bucket solution
class HitCounter3:
    def __init__(self):
        self.window_size = 300
        self.buckets = [None] * self.window_size

    def hit(self, timestamp):
        index = timestamp % self.window_size
        if self.buckets[index] is None:
            self.buckets[index] = [timestamp, 1]
            return

        old_time, old_count = self.buckets[index]
        if old_time < timestamp:
            self.total -= old_count
            self.buckets[index] = [timestamp, 1]
        else:  # old time is equal to the timestamp
            self.buckets[index][1] += 1

    def getHits(self, timestamp):
        total = 0
        for bt in self.buckets:
            if bt and timestamp - bt[0] < self.window_size:
                total += bt[1]
        return total
