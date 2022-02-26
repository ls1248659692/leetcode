# The trie is a tree of nodes which supports Find and Insert operations. It is also called prefix tree.
# trie tree is built to help match the whole words list in one batch.
# Scenario: autocomplete, spell checker, IP routing, T9 predictive text, solving word games.
# just basic version, improvement like: double-array trie, tail compressed
#
# words list has k words, the max word len is m
# Time:  O(m) for match once
# Space: O(mk)


# dict version
def trie_tree_template(word_to_match: str, words_to_build: 'List[str]'):
    # create trie tree
    trie = {}
    # or use autovivification
    # trie_tree = lambda: defaultdict(trie_tree)
    # def trie_tree(): return defaultdict(trie_tree)
    # trie = trie_tree()

    # add words recursively
    for w in words_to_build:
        cur = trie
        for c in w:
            cur = cur.setdefault(c, {})
        # end flag, record the whole words, or other data as you need
        cur['#'] = w

    # traverse with trie tree
    cur, res = trie, []
    for c in word_to_match:
        if c not in cur:
            # match failed
            break
        # prefix matched
        cur = cur[c]

    # the whole word matched
    if "#" in cur:
        res.append(cur['#'])


ALPHABET_SIZE = 26


# object-oriented array version
class TrieNode:
    def __init__(self):
        self.children = [None] * ALPHABET_SIZE
        # is_end_of_word is True if node represent the end of the word
        self.is_end_of_word = False
