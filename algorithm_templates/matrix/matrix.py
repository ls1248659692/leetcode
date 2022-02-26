# common operations of matrix with examples
# here matrix just represents 2-dimension array, not including matrix operation in math
from collections import defaultdict

'''
matrix neighbors traversal
'''


# simulation
def traverse_neighbor(self, matrix):
    if not matrix or not matrix[0]:
        return

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # construct neighbor iterator
            for I, J in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                # check boundary
                if 0 <= I < len(matrix) and 0 <= J < len(matrix[0]):
                    '''
                    neighbor logic process
                    '''
                    self.process_logic(matrix[I][J])


# use one-dimensional dict, and access neighbors by complex number
def traverse_neighbor_by_complex(self, board):
    board = {i + 1j * j: v for i, row in enumerate(board) for j, v in enumerate(row)}
    for z in board:
        # get neighbor by complex number operation
        for k in range(4):
            '''
            neighbor logic process
            '''
            self.process_neighor_logic(board.get(z + 1j ** k))


'''
matrix analog anti-analog traversal
'''


# simulation, in place, without extra space
def traverse_analogs(self, M):
    if not M or not M[0]:
        return
    m, n = len(M), len(M[0])
    for i, j in [(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)]:
        # calculate the size of analog
        size = min(m - i, n - j)
        for k in range(size):
            '''
            analog logic process here
            '''
            self.process_analog_logic(M[i + k][j + k])

    # check anti-analog
    for i, j in [(i, n - 1) for i in range(m)] + [(0, j) for j in range(n - 1)]:
        # calculate the size of anti-analog
        size = min(m - i, n - m + j + 1)
        for k in range(size):
            '''
            anti-analog logic process here
            '''
            self.process_anti_analog_logic(M[i + k][j - k])


# use list, similar to dp
def longestLine1(M):
    if not M or not M[0]:
        return 0

    m, n = len(M), len(M[0])

    ver = [0] * n
    dia = [0] * (n + 1)
    anti_dia = [0] * (n + 1)

    max_count = 0
    for row in range(m):
        hor = 0
        temp_dia = [0] * (n + 1)
        temp_anti_dia = [0] * (n + 1)
        for col in range(n):
            if M[row][col] == 0:
                ver[col] = 0
                temp_dia[col + 1] = 0
                temp_anti_dia[col] = 0
                hor = 0
            else:
                hor += 1
                ver[col] += 1
                temp_dia[col + 1] = dia[col] + 1
                temp_anti_dia[col] = anti_dia[col + 1] + 1
                max_count = max(max_count, hor, ver[col], temp_dia[col + 1], temp_anti_dia[col])
        dia, anti_dia = temp_dia, temp_anti_dia
    return max_count


# merge dict together by fractions or complex
def longestLine2(M):
    max_len = 0
    # merge dict together by fractions
    cur_len = defaultdict(int)
    for i, row in enumerate(M):
        for j, v in enumerate(row):
            # analog: i+j, anti-analog: i-j
            for key in i, j + .1, i + j + .2, i - j + .3:
                # accumulate util v turn to zero
                cur_len[key] = (cur_len[key] + 1) * v
                max_len = max(max_len, cur_len[key])
    return max_len


'''
transpose matrix
'''


def transpose(A):
    return list(map(list, zip(*A)))


'''
spiral matrix
'''


# simulation, rotate direction: di, dj = dj, -di   i.e. (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0) -> (0, 1)
def generate_spiral_matrix(n):
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


# use zip
# |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
# |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
# |7 8 9|      |4 7|
def traverse_spiral_order(matrix):
    # [*...] = list(), [*zip(*matrix)]: transpose matrix
    return matrix and [*matrix.pop(0)] + traverse_spiral_order([*zip(*matrix)][::-1])


# use zip
# ||  =>  |9|  =>  |8|      |6 7|      |4 5|      |1 2 3|
#                  |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
#                                      |8 7|      |7 6 5|
def generate_spiral_matrix_zip(n):
    M, lo = [], n * n + 1
    while lo > 1:
        lo, hi = lo - len(M), lo
        # M = [[*range(lo, hi)]] + [*map(list, zip(*M[::-1]))]
        M = [list(range(lo, hi))] + list(map(list, zip(*M[::-1])))
    return M
