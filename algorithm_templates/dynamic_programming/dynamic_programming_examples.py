from bisect import bisect_left


# [322] https://leetcode.com/problems/coin-change/
# compute the fewest number of coins that you need to make up that amount
def coinChange(coins, amount):
    MAX = float('inf')
    dp = [0] + [MAX] * amount

    for i in range(1, amount + 1):
        dp[i] = min(dp[i - c] if i - c >= 0 else MAX for c in coins) + 1

    # more pythonic way, bool as index
    return [dp[-1], -1][dp[-1] == MAX]


# [300] https://leetcode.com/problems/longest-increasing-subsequence/
# Given an unsorted array of integers, find the length of longest increasing sub-sequence.
#
# dp O(n^2)
def lengthOfLIS1(nums: 'List[int]') -> int:
    if not nums: return 0
    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    return max(dp)


# [300] https://leetcode.com/problems/longest-increasing-subsequence/
# Given an unsorted array of integers, find the length of longest increasing sub-sequence.
#
# dp with binary search O(nlog(n))
def lengthOfLIS2(nums: 'List[int]') -> int:
    dp = [0] * len(nums)

    length = 0
    for num in nums:
        i = bisect_left(dp, num, 0, length)
        if i < 0:
            i = -(i + 1)
        dp[i] = num
        if i == length:
            length += 1
    return length


# [72] https://leetcode.com/problems/edit-distance/
# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
def minDistance(word1: 'str', word2: 'str') -> 'int':
    m, n = len(word1), len(word2)

    # states definition: cur_min_edit_dist
    # states compressed to two states: old and new
    dp = [[0] * (m + 1) for _ in range(2)]

    # initialize the initial edit distance, add one more state for init state
    for i in range(0, m + 1):
        dp[0][i] = i

    cur = 1
    for i in range(n):
        # initialize the init state
        dp[cur][0] = i + 1
        for j in range(m):
            # state transition equation
            # if char matched, this is the min dist.
            if word1[j] == word2[i]:
                dp[cur][j + 1] = dp[cur ^ 1][j]
            # otherwise, 1 + minimum of edit/remove/add operations
            else:
                dp[cur][j + 1] = 1 + min(dp[cur ^ 1][j], dp[cur ^ 1][j + 1], dp[cur][j])
        # switch with two states
        cur ^= 1
    return dp[cur ^ 1][-1]


# [375] https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.
#
# Bottom-up dynamic programming
def getMoneyAmount(n):
    need = [[0] * (n + 1) for _ in range(n + 1)]
    for lo in range(n, 0, -1):
        for hi in range(lo + 1, n + 1):
            need[lo][hi] = min(x + max(need[lo][x - 1], need[x + 1][hi])
                               for x in range(lo, hi))
    return need[1][n]


# Top-down with memoization
def getMoneyAmount(n):
    class Need(dict):
        def __missing__(self, miss):
            lo, hi = miss
            if lo >= hi:
                return 0
            ret = self[lo, hi] = min(x + max(self[lo, x - 1], self[x + 1, hi])
                                     for x in range(lo, hi))
            return ret

    return Need()[1, n]


# [562] https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
# find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
#
# 3D DP
def longestLine1(M: 'List[List[int]]') -> int:
    if len(M) == 0:
        return 0

    dp = [[[0, 0, 0, 0] for _ in range(len(M[0]))] for _ in range(len(M))]
    max_len = 0
    for row in range(len(M)):
        for col in range(len(M[0])):
            if M[row][col] == 1:
                dp[row][col][0] = dp[row][col - 1][0] + 1 if col > 0 else 1
                dp[row][col][1] = dp[row - 1][col][1] + 1 if row > 0 else 1
                dp[row][col][2] = dp[row - 1][col - 1][2] + 1 if row > 0 and col > 0 else 1
                dp[row][col][3] = dp[row - 1][col + 1][3] + 1 if row > 0 and col < len(M[0]) - 1 else 1
                max_len = max(max_len, dp[row][col][0], dp[row][col][1], dp[row][col][2], dp[row][col][3])

    return max_len


# [562] https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
# find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
#
# compress to 2D DP
def longestLine2(M: 'List[List[int]]') -> int:
    if len(M) == 0:
        return 0

    dp = [[0, 0, 0, 0] for _ in range(len(M[0]))]
    max_len = 0
    for i in range(len(M)):
        old = 0
        for j in range(len(M[0])):
            if M[i][j] == 1:
                dp[j][0] = dp[j - 1][0] + 1 if j > 0 else 1
                dp[j][1] = dp[j][1] + 1 if i > 0 else 1
                # analog need cache pre node, because it will be overwrite
                prev = dp[j][2]
                dp[j][2] = old + 1 if i > 0 and j > 0 else 1
                old = prev
                dp[j][3] = dp[j + 1][3] + 1 if i > 0 and j < len(M[0]) - 1 else 1
                max_len = max(max_len, dp[j][0], dp[j][1], dp[j][2], dp[j][3])
            else:
                # because of reuse, should reset the state
                old = dp[j][2]
                dp[j][0] = dp[j][1] = dp[j][2] = dp[j][3] = 0
    return max_len


# [188] https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# stock problems can reference to this:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
def maxProfit(k: int, prices: 'List[int]') -> int:
    if not prices:
        return 0

    n = len(prices)
    # state: max profit util today, 0: occupy 0, can buy in, 1: occupy 1, can sell out

    # if k >= n-1, maximum trade count in n day, considered as unlimited transaction, turn to greedy algorithm
    if k >= n - 1:
        max_profit = 0
        for i in range(n - 1):
            max_profit = max_profit + (prices[i + 1] - prices[i] if prices[i + 1] - prices[i] > 0 else 0)
        return max_profit

    # initialization, first day of trade, and state before first trade
    mp = [[0 for _ in range(n)] for _ in range(2)]
    mp[1][0] = -prices[0]
    for i in range(1, n):
        mp[0][i] = 0
        mp[1][i] = max(-prices[i], mp[1][i - 1])

    for i in range(1, k + 1):
        mp2 = [[0 for _ in range(n)] for _ in range(2)]
        mp2[1][0] = -prices[0]
        for j in range(1, n):
            # state transition equation
            # occupy 0: do nothing, or sell out
            mp2[0][j] = max(mp2[0][j - 1], mp[1][j - 1] + prices[j])
            # occupy 1: do nothing, or buy in
            mp2[1][j] = max(mp2[1][j - 1], mp2[0][j - 1] - prices[j])
        mp = mp2

    return mp[0][-1]


# [188] https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
def maxProfit2(k: int, prices: 'List[int]') -> int:
    if not prices or k == 0:
        return 0
    n = len(prices)
    if k >= n / 2:
        return sum(a - b for a, b in zip(prices[1:], prices[:-1]) if a > b)
    local_max = [0] * (k + 1)
    global_max = [0] * (k + 1)
    for i in range(1, n):
        diff = prices[i] - prices[i - 1]
        for j in range(k, 0, -1):
            local_max[j] = max(local_max[j], global_max[j - 1]) + diff
            global_max[j] = max(local_max[j], global_max[j])
    return global_max[k]


# [32] https://leetcode.com/problems/longest-valid-parentheses/
# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.
def longestValidParentheses(s):
    # let dp[i] is the number of longest valid Parentheses ended with the i - 1 position of s,
    # then we have the following relationship:
    # dp[i + 1] = dp[p] + i - p + 1 where p is the position of '(' which can matches current ')' in the stack.
    dp, stack = [0] * (len(s) + 1), []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                p = stack.pop()
                dp[i + 1] = dp[p] + i - p + 1
    return max(dp)
