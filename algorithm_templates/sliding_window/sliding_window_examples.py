from collections import Counter
from collections import defaultdict


# [3] https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.
#
# variation with no pattern
def lengthOfLongestSubstring(s):
    # create a default dict to maintain state
    counter = defaultdict(int)
    count, start, end, res = 0, 0, 0, 0
    while end < len(s):
        counter[s[end]] += 1
        if counter[s[end]] > 1:
            count += 1
        end += 1
        while count > 0:
            counter[s[start]] -= 1
            if counter[s[start]] > 0:
                count -= 1
            start += 1
        res = max(res, end - start)
    return res


# [76] https://leetcode.com/problems/minimum-window-substring/
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T
#
# variation with finding minimum
def minWindow(s: str, t: str) -> str:
    counter = Counter(t)
    count, start, end, res = len(t), 0, 0, [float('inf'), 0]
    while end < len(s):
        counter[s[end]] -= 1
        # consider duplicate char in t
        if counter[s[end]] >= 0:
            count -= 1
        end += 1
        # valid in while
        while count == 0:
            # update minimum here, inner while loop
            if end - start < res[0]:
                res = (end - start, start)

            counter[s[start]] += 1
            if counter[s[start]] > 0:
                count += 1
            start += 1
    return s[res[1]:res[0] + res[1]] if res[0] != float('inf') else ''


# [904] https://leetcode.com/problems/fruit-into-baskets/
# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
# What is the total amount of fruit you can collect with this procedure?
#
# variation with list
def totalFruit(tree: 'List[int]') -> int:
    counter = defaultdict(int)
    count, start, end, res = 0, 0, 0, 0

    while end < len(tree):
        counter[tree[end]] += 1
        if counter[tree[end]] == 1:
            count += 1
        end += 1
        while count > 2:
            counter[tree[start]] -= 1
            if counter[tree[start]] == 0:
                count -= 1
            start += 1
        res = max(res, end - start)
    return res


# [438] https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# variation with restrict between start and end
def findAnagrams(s: str, p: str) -> 'List[int]':
    len_p, len_s = len(p), len(s)
    if len_p > len_s:
        return []
    counter = Counter(p)
    count, start, end, res = len_p, 0, 0, []

    while end < len_s:
        # only update counter when match char in p
        counter[s[end]] -= 1
        if counter[s[end]] >= 0:
            count -= 1
        end += 1

        if count == 0:
            res.append(start)

        # not use a while, because restrict the length
        if end - start == len_p:
            counter[s[start]] += 1
            # exclude char not in p, because always negative
            if counter[s[start]] > 0:
                count += 1
            start += 1
    return res


# [30] https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
# variation with complex match policy
def findSubstring(s: str, words: 'List[str]') -> 'List[int]':
    if not words:
        return []

    word_len, res = len(words[0]), []

    # start offset from 0 to word_len, and step is word_len
    for i in range(word_len):
        # reset state every epoch
        counter = Counter(words)
        start, end, count = i, i, len(words)
        while end < len(s):
            cur_word = s[end:end + word_len]
            # check is not necessary here, just for performance
            if cur_word in counter:
                counter[cur_word] -= 1
                if counter[cur_word] >= 0:
                    count -= 1
            end += word_len

            if count == 0:
                res.append(start)

            # ensure consecutive words
            if end - start == word_len * len(words):
                cur_word = s[start:start + word_len]
                if cur_word in counter:
                    counter[cur_word] += 1
                    if counter[cur_word] > 0:
                        count += 1
                start += word_len

    # the order is not necessary here
    return res