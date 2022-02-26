from collections import Counter
import re


# [46] https://leetcode.com/problems/permutations/
# Given a collection of distinct integers, return all possible permutations.
def permute(nums):
    def backtrack(first=0):
        # if all integers are used up
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            # place i-th integer first
            # in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # use next integers to complete the permutations
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    backtrack()
    return output


# [51] https://leetcode.com/problems/n-queens/
# Given an integer n, return all distinct solutions to the n-queens puzzle.
def solveNQueens(n):
    result = []

    def backtracking(queens, xy_diff, xy_sums):
        p = len(queens)
        if p == n:
            result.append(queens)
            return
        for q in range(n):
            if q not in queens and p - q not in xy_diff and p + q not in xy_sums:
                backtracking(queens + [q], xy_diff | {p - q}, xy_sums | {p + q})

    backtracking([], set(), set())
    return [['.' * i + 'Q' + '.' * (n - i - 1) for i in queen] for queen in result]


# [37] https://leetcode.com/problems/sudoku-solver/
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# easy-understanding version, not a efficient solution
# optimize: use priority queue and bit-manipulation
def solveSudoku(board):
    stack = [(i, j) for i in range(9) for j in range(9) if board[i][j] == "."]

    def dfs():
        if not stack:
            return
        x, y = stack.pop()
        box = [board[x // 3 * 3 + i][y // 3 * 3 + j] for i in range(3) for j in range(3)]
        row = [board[x][j] for j in range(9)]
        col = [board[i][y] for i in range(9)]
        for i in "123456789":
            if not any([i in box, i in col, i in row]):
                board[x][y] = i
                dfs()
                if not stack:
                    return
        board[x][y] = "."
        stack.append((x, y))

    dfs()


# [79] https://leetcode.com/problems/word-search/
# Given a 2D board and a word, find if the word exists in the grid.
def exist(board: 'List[List[str]]', word: str) -> bool:
    m, n = len(board), len(board[0])
    bcnts = Counter(c for r in board for c in r)

    for w, w_cnt in Counter(word).items():
        if w not in bcnts or w_cnt > bcnts[w]:
            return False

    def backtrack(i, j, index):
        if index == len(word) - 1:
            return True

        # mark it as visited
        board[i][j] = '*'
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            next_i, next_j = i + dx, j + dy
            # check before dfs
            if 0 <= next_i < m and 0 <= next_j < n and word[index + 1] == board[next_i][next_j] and backtrack(
                    next_i, next_j, index + 1):
                return True

        # revert the state
        board[i][j] = word[index]
        return False

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0] and backtrack(i, j, 0):
                return True

    return False


# [351] https://leetcode.com/problems/android-unlock-patterns/
# Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of
# unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.
def numberOfPatterns(m: int, n: int) -> int:
    through_dict = {(1, 3): 2, (4, 6): 5, (7, 9): 8, (1, 7): 4, (2, 8): 5, (3, 9): 6, (1, 9): 5, (3, 7): 5}
    res = 0

    def backtracking(last, used: set, left: set):
        nonlocal res
        if len(used) > n:
            return
        if m <= len(used) <= n:
            res += 1

        for num in left:
            if last:
                key = (last, num) if last < num else (num, last)
                if key in through_dict:
                    if through_dict[key] in left:
                        continue
            used.add(num)
            left.remove(num)
            backtracking(num, used, left)
            left.add(num)
            used.remove(num)

    backtracking(None, set(), {i for i in range(1, 10)})
    return res


# [90] https://leetcode.com/problems/subsets-ii/
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
def subsetsWithDup(nums: 'List[int]') -> 'List[List[int]]':
    res = []
    nums.sort()

    def backtracking(start, path):
        # abandon rest numbers
        res.append(path)
        for i in range(start, len(nums)):
            # duplicate element will only add the first one, and skip all nums after it.
            # equivalent to internal serial number for same element
            if i > start and nums[i] == nums[i - 1]:
                continue
            backtracking(i + 1, path + [nums[i]])

    backtracking(0, [])
    return res


# [10] https://leetcode.com/problems/regular-expression-matching/
# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# The key point to enhance performance is pre-processing pattern
# specific optimization, not very scalable, but efficient for this solution.
def isMatch(s, p):
    pattern = re.compile(r'[a-z.]\*?')
    patterns = re.findall(pattern, p)

    # specific optimization, not scalable, but efficient for this solution
    # pre-process patterns, merge same or including patterns
    def preProcess(patterns):
        # .* merge all adjacent x* pattern
        p_count, p_index = 0, -1
        # count every time after update patterns
        while p_count < patterns.count('.*'):
            index = patterns.index('.*', p_index + 1)
            index_l, index_r = index - 1, index + 1
            while index_l >= 0 and len(patterns[index_l]) == 2:
                index_l -= 1
            while index_r < len(patterns) and len(patterns[index_r]) == 2:
                index_r += 1

            patterns = patterns[0:index_l + 1] + patterns[index:index + 1] + patterns[index_r:]
            # update p_index after merge
            p_index = patterns.index('.*', p_index + 1)
            p_count += 1

        # merge a-z* merge all adjacent corresponding a-z and a-z*
        start_index, i, flag, pattern_ch, new_patterns = 0, 0, False, '', []
        for i, pat in enumerate(patterns):
            if pattern_ch != pat or pattern_ch[0] == '.':
                if flag:
                    new_patterns.append(pattern_ch)
                else:
                    new_patterns.extend(patterns[start_index:i])

                flag = len(pat) == 2
                start_index = i
                pattern_ch = pat
            elif not flag and len(pat) == 2:
                flag = True

        if flag:
            new_patterns.append(pattern_ch)
        else:
            new_patterns.extend(patterns[start_index:i + 1])

        return new_patterns

    # match pattern by backtracking
    def isMatchPatterns(s, patterns, index):
        # if patterns has been matched out, check whether reach the end of s
        if len(patterns) == 0:
            return index >= len(s)

        # if there are remain patterns, if all the remains like x*, match success, otherwise failed.
        if index >= len(s):
            return all(len(p) > 1 for p in patterns)

        p = patterns[0]
        if len(p) == 1:
            # when single pattern, if encounter same char or '.', match success, otherwise failed
            if p[0] == s[index] or p[0] == '.':
                return isMatchPatterns(s, patterns[1:], index + 1)
            else:
                return False
        elif len(p) == 2:
            # when pattern with *, if encounter same char or '.', match success, otherwise failed
            if p[0] == s[index] or p[0] == '.':
                # when match success, you can continue to use this pattern, or abandon this and match next pattern.
                return isMatchPatterns(s, patterns, index + 1) or isMatchPatterns(s, patterns[1:], index)
            # when it failed, match next pattern, not return false, because * can match zero char.
            else:
                return isMatchPatterns(s, patterns[1:], index)

    return isMatchPatterns(s, preProcess(patterns), 0)
