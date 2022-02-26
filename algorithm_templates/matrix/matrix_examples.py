from bisect import bisect_left
from itertools import zip_longest


# [48] https://leetcode.com/problems/rotate-image/
# Rotate the image by 90 degrees (clockwise)
#
# clean most pythonic
def rotate1(A):
    # the the result rows are actually tuples, not lists, so it's a bit dirty. To fix this, we can just apply list to every row
    A[:] = map(list, zip(*A[::-1]))


# [48] https://leetcode.com/problems/rotate-image/
# Rotate the image by 90 degrees (clockwise)
#
# use ~ in slice
def rotate2(A):
    n = len(A)
    for i in range(n // 2):
        for j in range(n - n // 2):
            A[i][j], A[~j][i], A[~i][~j], A[j][~i] = A[~j][i], A[~i][~j], A[j][~i], A[i][j]


# [48] https://leetcode.com/problems/rotate-image/
# Rotate the image by 90 degrees (clockwise)
#
# list comprehension
def rotate3(A):
    A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]


# [54] https://leetcode.com/problems/spiral-matrix/
# return all elements of the matrix in spiral order
# |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
# |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
# |7 8 9|      |4 7|
def spiralOrder1(self, matrix):
    # and return right value
    return matrix and [*matrix.pop(0)] + self.spiralOrder1([*zip(*matrix)][::-1])


# [59] https://leetcode.com/problems/spiral-matrix-ii/
# generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# simulation
def generateMatrix1(n):
    M = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(n * n):
        M[i][j] = k + 1
        # also include reaching boundary edge case
        if M[(i + di) % n][(j + dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj
    return M


# [59] https://leetcode.com/problems/spiral-matrix-ii/
# generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# use zip
def generateMatrix2(n):
    M, lo = [], n * n + 1
    while lo > 1:
        lo, hi = lo - len(M), lo
        M = [list(range(lo, hi))] + list(map(list, zip(*M[::-1])))
    return M


# [695] https://leetcode.com/problems/max-area-of-island/
# Find the maximum area of an island in the given 2D array.
#
# complex number & dict pop, map, sum
def maxAreaOfIsland(grid):
    grid = {i + j * 1j: val for i, row in enumerate(grid) for j, val in enumerate(row)}

    def area(z):
        return grid.pop(z, 0) and 1 + sum(area(z + 1j ** k) for k in range(4))

    return max(map(area, set(grid)))


# [422] https://leetcode.com/problems/valid-word-square/
# Given a sequence of words, check whether it forms a valid word square.
#
# The map(None, ...) transposes the "matrix", filling missing spots with None, not worked in Python3
def validWordSquare1(words):
    return map(None, *words) == map(None, *map(None, *words))


def validWordSquare2(words):
    f = lambda x: map(None, *x)  # padded Transpose
    return f(f(words)) == f(words)


def validWordSquare3(words: 'List[str]') -> 'bool':
    for i, tup in enumerate(zip_longest(*words, fillvalue='')):
        if ''.join(tup) != words[i]:
            return False
    return True


def validWordSquare4(words):
    return map("".join, zip_longest(*words, fillvalue='')) == words


def validWordSquare5(words):
    other = list(zip_longest(*words))
    return not any(i >= len(other) or j >= len(other[i]) or other[i][j] != char
                   for i, word in enumerate(words)
                   for j, char in enumerate(word))


# [240] https://leetcode.com/problems/search-a-2d-matrix-ii/
# Write an efficient algorithm that searches for a value in matrix which sorted in each row and column
#
# binary search reduction
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    start_r, end_r, start_c, end_c = 0, m - 1, 0, n - 1

    while start_r <= end_r and start_c <= end_c:
        # compare first in column
        row = matrix[start_r][start_c:end_c + 1]
        idx = bisect_left(row, target)
        if idx < len(row) and row[idx] == target:
            return True
        end_c = start_c + idx - 1

        # compare first in row
        col = [matrix[i][start_c] for i in range(start_r, end_r + 1)]
        idx = bisect_left(col, target)
        if idx < len(col) and col[idx] == target:
            return True
        end_r = start_r + idx - 1

        # compare last in column
        row = matrix[end_r][start_c:end_c + 1]
        idx = bisect_left(row, target)
        if idx < len(row) and row[idx] == target:
            return True
        start_c += idx

        # compare last in row
        col = [matrix[i][end_c] for i in range(start_r, end_r + 1)]
        idx = bisect_left(col, target)
        if idx < len(col) and col[idx] == target:
            return True
        start_r += idx

    return False


# [240] https://leetcode.com/problems/search-a-2d-matrix-ii/
# Write an efficient algorithm that searches for a value in matrix which sorted in each row and column
#
# Divide and Conquer
def searchMatrix1(matrix, target):
    # an empty matrix obviously does not contain `target`
    if not matrix:
        return False

    def search_rec(left, up, right, down):
        # this submatrix has no height or no width.
        if left > right or up > down:
            return False
        # `target` is already larger than the largest element or smaller
        # than the smallest element in this submatrix.
        elif target < matrix[up][left] or target > matrix[down][right]:
            return False

        mid = left + (right - left) // 2

        # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
        row = up
        while row <= down and matrix[row][mid] <= target:
            if matrix[row][mid] == target:
                return True
            row += 1

        return search_rec(left, row, mid - 1, down) or search_rec(mid + 1, up, right, row - 1)

    return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


# [240] https://leetcode.com/problems/search-a-2d-matrix-ii/
# Write an efficient algorithm that searches for a value in matrix which sorted in each row and column
#
# O(m+n) search space reduction
def searchMatrix2(matrix, target):
    # an empty matrix obviously does not contain `target` (make this check
    # because we want to cache `width` for efficiency's sake)
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    # cache these, as they won't change.
    height = len(matrix)
    width = len(matrix[0])

    # start our "pointer" in the bottom-left
    row = height - 1
    col = 0

    while col < width and row >= 0:
        if matrix[row][col] > target:
            row -= 1
        elif matrix[row][col] < target:
            col += 1
        else:  # found it
            return True

    return False
