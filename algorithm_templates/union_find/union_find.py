# Union find, also called Disjoint-set, tracks a set of elements partitioned into a number of disjoint (non-overlapping) subsets
# optimized by rank and path compression
#
# Time Complexity: Total Number of operations=(N+P). Number of nodes=2*P Thus time complexity=O((N+P)* alpha(P)) alpha(P)
# (Also know as Inverse-Ackermann function) grows very slowly and will always be less than or equal to 5.
#
# Time:  O(n)
# Space: O(n)


# light weight version, defined in logic
def in_union_find_logic():
    parent, rank = {}, {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            if rank[x] < rank[y]:
                x, y = y, x
            parent[y] = x
            rank[x] += rank[x] == rank[y]

    # non-essential functions
    def is_connected(x, y):
        return find(x) == find(y)

    def create(v):
        x = parent[x] = v
        rank[x] = 0
        return x


# full object-oriented version
class Union:
    def __init__(self, value):
        self.v = value
        self.root = self
        self.rank = 0


class UnionFind:
    def __init__(self):
        self.us = {}

    def create_union(self, value):
        u = Union(value)
        self.us[u.v] = u
        return u

    # recursion version, more concise
    def find(self, x):
        if x.root != x:
            # find root & path compression
            x.root = self.find2(x.root)
        return x.root

    # iteration version, less cost, without call stack
    def find2(self, x):
        cur = x
        # find root
        while cur.root != cur:
            cur = cur.root
        root = cur
        # path compression
        while x.root != root:
            # rank update is not necessary here, because we only need to keep rank relative relation
            # x, x.root, x.rank = x.root, root, 1
            x, x.root = x.root, root
        return root

    # normal version, more easy-understanding
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            # union by rank
            if x.rank < y.rank:
                x.root = y
            elif x.rank > y.rank:
                y.root = x
            else:
                y.root = x
                x.rank += 1

    # swap version, more concise
    def union2(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            # union by rank
            if x.rank < y.rank:
                x, y = y, x
            y.root = x
            x.rank += x.rank == y.rank


# id_map version
class UnionFind2:
    # initialization n union_set
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # without rank
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    # with rank
    def union2(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            # union by rank
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            self.parent[y] = x
            self.rank[x] += self.rank[x] == self.rank[y]

    # logic example code
    def union_find_logic(self, pairs):
        i = 0  # id of word
        word_id = {}  # word -> ID

        dsu = UnionFind2(2 * len(pairs))  # restrict with the capacity

        for w1, w2 in pairs:
            # build the map, like word vocabulary
            if w1 not in word_id:
                word_id[w1] = i
                i += 1
            if w2 not in word_id:
                word_id[w2] = i
                i += 1
            dsu.union(word_id[w1], word_id[w2])  # union
