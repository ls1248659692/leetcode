# [323] https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to find the number of connected components in an undirected graph.
def countComponents(n: int, edges: 'List[List[int]]') -> int:
    roots = [i for i in range(n)]

    # iteration version
    def find(x):
        root = x
        while root != roots[root]:
            root = roots[root]
        # path compression
        while x != roots[x]:
            x, roots[x] = roots[x], root
        return root

    # without rank
    def union(x, y):
        roots[find(x)] = find(y)

    for x, y in edges:
        union(x, y)

    return len(set([find(x) for x in roots]))

# [305] https://leetcode.com/problems/number-of-islands-ii/
# Given a list of positions to operate, count the number of islands after each addLand operation.
#
# light-weight version
def numIslands2(m, n, positions):
    parent, rank, count = {}, {}, 0

    # recursion version
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # with rank
    def union(x, y):
        nonlocal count
        x, y = find(x), find(y)
        if x != y:
            if rank[x] < rank[y]:
                x, y = y, x
            parent[y] = x
            rank[x] += rank[x] == rank[y]
            count -= 1

    def add(pos):
        nonlocal count
        i, j = pos
        x = parent[x] = i, j
        rank[x] = 0
        count += 1
        for y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
            if y in parent:
                union(x, y)
        return count

    return list(map(add, positions))


# [305] https://leetcode.com/problems/number-of-islands-ii/
# Given a list of positions to operate, count the number of islands after each addLand operation.
#
# full object oriented version
class Union:
    def __init__(self, value):
        self.v = value
        self.root = self
        self.rank = 0


class UnionFind:
    # path compress and rank
    def __init__(self):
        self.us = {}
        self.count = 0

    def create_union(self, value):
        u = Union(value)
        self.us[u.v] = u
        self.count += 1
        return u

    def find(self, x):
        cur = x

        while cur.root != cur:
            cur = cur.root
        root = cur
        while x.root != root:
            x, x.root, x.rank = x.root, root, 1
        return root

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.count -= 1
        if x_root.rank < y_root.rank:
            x_root.root = y_root
        elif x_root.rank > y_root.rank:
            y_root.root = x_root
        else:
            x_root.root = y_root
            y_root.rank += 1


def numIslands21(m: int, n: int, positions: 'List[List[int]]') -> 'List[int]':
    us = UnionFind()
    res = []
    for i, j in positions:
        new_island = us.create_union((i, j))
        for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if 0 <= I < m and 0 <= J < n and (I, J) in us.us:
                us.union(us.us[(I, J)], new_island)

        res.append(us.count)
    return res


# [737] https://leetcode.com/problems/sentence-similarity-ii/
# Given two sentences words1, words2, and a list of similar word pairs pairs, determine if two sentences are similar.
class UnionFind2:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        self.parent[p_x] = p_y


def areSentencesSimilarTwo(words1, words2, pairs):
    if len(words1) != len(words2):
        return False
    i = 0  # id of word
    word2id = {}  # word -> ID

    uf = UnionFind2(2 * len(pairs))  # restrict with the capacity

    for w1, w2 in pairs:
        if w1 not in word2id:  # build the map, like word vocabulary
            word2id[w1] = i
            i += 1
        if w2 not in word2id:
            word2id[w2] = i
            i += 1
        uf.union(word2id[w1], word2id[w2])  # union

    for w1, w2 in zip(words1, words2):
        if w1 == w2:  # corner case: similar to itself
            continue
        if w1 not in word2id or w2 not in word2id:  # corner case: words1 or words2 no in pairs
            return False
        if uf.find(word2id[w1]) != uf.find(word2id[w2]):
            return False
    return True


# [399] https://leetcode.com/problems/evaluate-division/
# Equations are given in the format A / B = k, where A and B are variables represented as strings,
# and k is a real number (floating point number). Given some queries, return the answers.
class DJS:
    def __init__(self, alphabet):
        self.parent = {char: char for char in alphabet}
        self.vals = {char: 1.0 for char in alphabet}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x], val = self.find(self.parent[x])
            self.vals[x] *= val
        return self.parent[x], self.vals[x]

    def union(self, y, x, val):
        x, val_x = self.find(x)
        y, val_y = self.find(y)
        if x == y: return
        self.parent[y] = self.parent[x]
        self.vals[y] = val * val_x / val_y


def calcEquation(equations: 'List[List[str]]', values: 'List[float]',
                 queries: 'List[List[str]]') -> 'List[float]':
    alphabet = set(sum(equations, []))
    ufo = DJS(alphabet)
    for (y, x), val in zip(equations, values):
        ufo.union(y, x, val)

    res = []
    for y, x in queries:
        if x not in alphabet or y not in alphabet:
            res.append(-1.0)
            continue
        y, val_y = ufo.find(y)
        x, val_x = ufo.find(x)
        if x == y:
            res.append(val_y / val_x)
        else:
            res.append(-1.0)
    return res
