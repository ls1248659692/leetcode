from collections import deque
from collections import defaultdict
from collections import Counter


# [111] https://leetcode.com/problems/minimum-depth-of-binary-tree/
# find the minimum depth of a binary tree.
def minDepth(root: 'TreeNode') -> int:
    if not root:
        return 0
    # push height and node into queue
    queue = [[1, root]]
    while queue:
        height, node = queue.pop(0)
        # reach the leaf
        if not node.left and not node.right:
            return height
        if node.left:
            queue.append((height + 1, node.left))
        if node.right:
            queue.append((height + 1, node.right))


# [513] https://leetcode.com/problems/find-bottom-left-tree-value/
# Given a binary tree, find the leftmost value in the last row of the tree.
#
# Doing BFS right-to-left means we can simply return the last node's value and don't have to keep track of the first
# node in the current row or even care about rows at all.
def findLeftMostNode(root):
    queue = [root]
    for node in queue:
        queue += filter(None, (node.right, node.left))
    return node.val


# [515] https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# find the largest value in each row of a binary tree.
def findValueMostElement(root):
    maxes = []
    row = [root]
    while row:
        maxes.append(max(node.val for node in row))
        row = [kid for node in row for kid in (node.left, node.right) if kid]
    return maxes


# [279] https://leetcode.com/problems/perfect-squares/
# given a positive integer n, find the least number of perfect square numbers
def numSquares(n: int) -> int:
    nums = [i * i for i in range(1, int(n ** 0.5) + 1)]
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        cur_value, step = queue.popleft()
        step += 1
        for num in nums:
            new_value = cur_value + num
            if new_value == n:
                return step
            elif new_value > n:
                break
            else:
                if new_value not in visited:
                    visited.add(new_value)
                    queue.append((new_value, step))


# [279] https://leetcode.com/problems/perfect-squares/
# given a positive integer n, find the least number of perfect square numbers
#
# bidirectional BFS, faster than one-directional BFS
def numSquares2(n):
    front, back, pm = [0], [n], 1  # pm is "plus minus"
    depth = [0] + [None] * (n - 1) + [-1]  # depth[0] == 0, depth[n] == -1, depth[everythingElse] == None
    while front:
        newFront = []
        for v in front:
            i = 1
            while True:
                w = v + pm * i * i  # generate a neighbor
                if w < 0 or w > n:  # all neighbors have been generated
                    break
                if depth[w] is None:  # w has not been discovered
                    depth[w] = depth[v] + pm  # mark it as discovered by assigning a depth to it
                    newFront.append(w)
                elif (depth[w] < 0) != (depth[v] < 0):  # w has been discovered in the `back` tree, so we're done
                    return abs(depth[w] - depth[v])
                i += 1
        front = newFront
        if len(front) > len(back):
            front, back, pm = back, front, -pm  # always expand the tree with fewer leaves


# [286] https://leetcode.com/problems/walls-and-gates/
# Fill each empty room with the distance to its nearest gate.
def wallsAndGates(rooms: 'List[List[int]]') -> None:
    bfs = [(i, j) for i, row in enumerate(rooms) for j, v in enumerate(row) if not v]
    for i, j in bfs:
        for I, J in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
            if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and rooms[I][J] > 2 ** 30:
                rooms[I][J] = rooms[i][j] + 1
                bfs += (I, J),


# [582] https://leetcode.com/problems/kill-process/
# Now given the two lists, and a PID representing a process you want to kill,
# return a list of PIDs of processes that will be killed in the end.
#
# pythonic-style BFS, concise and elegant
def killProcess(pid, ppid, kill):
    d = defaultdict(list)
    for c, p in zip(pid, ppid):
        d[p].append(c)
    bfs = [kill]
    # iterate while append, concise way but use more memory
    for i in bfs:
        bfs += d[i]
    return bfs


# [854] https://leetcode.com/problems/k-similar-strings/
# Given two anagrams A and B, return the smallest K for which A and B are K-similar.
def kSimilarity(A: str, B: str) -> int:
    def bfs(s, e):
        layer = [[s]]
        while True:
            next_layer = []
            while layer:
                path = layer.pop()
                curr = path[-1]
                if (curr, e) in counter:
                    return path + [e]
                for i in range(6):
                    if i not in path and (curr, i) in counter:
                        next_layer.append(path + [i])
            layer = next_layer

    counter = Counter()
    for i in range(len(A)):
        p, q = ord(A[i]) - 97, ord(B[i]) - 97
        if p != q:
            counter[(p, q)] += 1
    res = 0
    while counter:
        keys = list(counter.keys())
        best = [0] * 7
        for a, b in keys:
            path = bfs(b, a)
            if len(path) == 2:
                best = path
                break
            if len(best) > len(path):
                best = path
        a, b = best[-1], best[0]
        path = bfs(b, a)
        res += len(path) - 1
        for i in range(len(path) - 1):
            if counter[(path[i], path[i + 1])] <= 1:
                counter.pop((path[i], path[i + 1]))
            else:
                counter[(path[i], path[i + 1])] -= 1
        if counter[(a, b)] > 1:
            counter[(a, b)] -= 1
        else:
            counter.pop((a, b))
    return res
