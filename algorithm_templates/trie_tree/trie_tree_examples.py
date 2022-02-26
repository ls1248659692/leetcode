import heapq
from copy import copy


# [212] https://leetcode.com/problems/word-search-ii/
# Given a 2D board and a list of words from the dictionary, find all words in the board
def findWords(board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
    if not board or not board[0]:
        return []
    m, n = len(board), len(board[0])
    visited = [[0] * n for _ in range(m)]
    trie = {}
    for w in words:
        cur = trie
        for c in w:
            cur = cur.setdefault(c, {})
        # record the whole words
        cur['#'] = w

    res = set()

    def dfs(i, j, trie):
        if '#' in trie:
            res.add(trie['#'])

        for I, J in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
            if 0 <= I < m and 0 <= J < n and not visited[I][J] and board[I][J] in trie:
                visited[I][J] = 1
                dfs(I, J, trie[board[I][J]])
                visited[I][J] = 0

    for i in range(m):
        for j in range(n):
            if board[i][j] in trie:
                visited[i][j] = 1
                dfs(i, j, trie[board[i][j]])
                visited[i][j] = 0

    return list(res)


# [616] https://leetcode.com/problems/add-bold-tag-in-string/
# add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict
def addBoldTag(s: str, dict: 'List[str]') -> str:
    trie, n, intervals, res = {}, len(s), [], ""

    # create trie tree
    for w in dict:
        cur = trie
        for c in w:
            cur = cur.setdefault(c, {})
        cur["#"] = 1

    # interval merge
    def add_interval(interval):
        if intervals and intervals[-1][1] >= interval[0]:
            if intervals[-1][1] < interval[1]:
                intervals[-1][1] = interval[1]
        else:
            intervals.append(interval)

    # make max match and add to interval
    for i in range(n):
        cur, max_end = trie, None
        for j in range(i, n):
            if s[j] not in cur:
                break
            cur = cur[s[j]]
            if "#" in cur:
                max_end = j + 1
        # just need to add max-match interval
        if max_end:
            add_interval([i, max_end])

    # concat result
    res, prev_end = "", 0
    for start, end in intervals:
        res += s[prev_end:start] + '<b>' + s[start:end] + "</b>"
        prev_end = end
    return res + s[prev_end:]


# [642] https://leetcode.com/problems/design-search-autocomplete-system/
# Design a search autocomplete system for a search engine.
# For each character they type except '#', you need to return the top 3 historical hot sentences
# that have prefix the same as the part of sentence already typed.
class AutocompleteSystem:
    def __init__(self, sentences: 'List[str]', times: 'List[int]'):
        self.trie = {}
        self.size = 3
        self.cur_trie = self.trie
        self.cur_word = ''

        for s, t in zip(sentences, times):
            cur = self.trie
            for c in s:
                cur = cur.setdefault(c, {})
            cur['#'] = HeapItem(t, s)

        def dfs(trie):
            heap = []
            if '#' in trie:
                # ASCII-code order
                heapq.heappush(heap, copy(trie['#']))

            for c in trie:
                if c != '#' and c != '*':
                    # cache priority queue here
                    cur_heap = dfs(trie[c])
                    for item in cur_heap:
                        if len(heap) < self.size:
                            heapq.heappush(heap, copy(item))
                        else:
                            heapq.heappushpop(heap, copy(item))
            trie['*'] = heap
            return heap

        dfs(self.trie)

    def add_word(self):
        cur = self.trie
        for c in self.cur_word:
            if c not in cur:
                cur[c] = {}
                cur[c]['*'] = []
            cur = cur[c]
        if '#' not in cur:
            cur['#'] = HeapItem(1, self.cur_word)
        else:
            cur['#'].count += 1

        word_item = cur['#']

        cur = self.trie
        for c in self.cur_word:
            cur = cur[c]
            heap = cur['*']
            for i in range(len(heap)):
                if heap[i].word == word_item.word:
                    heap[i].count += 1
                    # heapq.heapify(heap)
                    heapq._siftup(heap, i)
                    break
            else:
                if len(heap) < self.size:
                    heapq.heappush(heap, copy(word_item))
                else:
                    heapq.heappushpop(heap, copy(word_item))

    def input(self, c: str) -> 'List[str]':
        res = []

        if c == '#':
            self.add_word()
            self.cur_trie = self.trie
            self.cur_word = ''
        else:
            self.cur_word += c

            if not self.cur_trie:
                return []
            if c not in self.cur_trie:
                self.cur_trie = None
                return []

            if c in self.cur_trie:
                self.cur_trie = self.cur_trie[c]
                if self.cur_trie['*']:
                    res = [item.word for item in sorted(self.cur_trie['*'], reverse=True)]

        return res


class HeapItem:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    # 解决ASCII-code排序问题
    def __lt__(self, other):
        if self.count != other.count:
            return self.count < other.count
        else:
            return self.word > other.word

    def __repr__(self):
        return self.word + ',' + str(self.count)

    def __copy__(self):
        return HeapItem(self.count, self.word)

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
