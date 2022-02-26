from itertools import groupby
from itertools import zip_longest
from functools import reduce
from collections import defaultdict
from collections import Counter
import string
import re
import operator


# [125] https://leetcode.com/problems/valid-palindrome/
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
def isPalindrome(s: str) -> bool:
    alphanumeric = ''.join(c for c in s.lower() if c.isalpha() or c.isdigit())
    return alphanumeric == alphanumeric[::-1]


# [151] https://leetcode.com/problems/reverse-words-in-a-string/
# Given an input string, reverse the string word by word.
def reverseWords(s: str) -> str:
    return ' '.join(s.strip().split()[::-1])


# [383] https://leetcode.com/problems/ransom-note/
#  write a function that will return true if the ransom note can be constructed from the magazines
def canConstruct(ransomNote: str, magazine: str) -> bool:
    return not Counter(ransomNote) - Counter(magazine)


# [557] https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
def reverseWords1(s: str) -> str:
    return ' '.join(map(lambda x: x[::-1], s.split(' ')))


def reverseWords2(s: str) -> str:
    return ' '.join(s.split()[::-1])[::-1]


# [796] https://leetcode.com/problems/rotate-string/
# Return True if and only if A can become B after some number of shifts on A.
#
# use in
def rotateString1(A: str, B: str) -> bool:
    return len(A) == len(B) and B in A + A


# circular array
def rotateString2(A: str, B: str) -> bool:
    if len(A) != len(B):
        return False
    if not A:
        return True
    n = len(A)
    for i in range(n):
        if all(A[(i + j) % n] == B[j] for j in range(n)):
            return True
    return False


# [389] https://leetcode.com/problems/find-the-difference/
# Find the letter that was added in t.
#
# use ord, rolling hash is another thought.
def findTheDifference1(s, t):
    return chr(sum(map(ord, t)) - sum(map(ord, s)))


# use xor to find the distinct number
def findTheDifference2(s, t):
    return chr(reduce(int.__xor__, map(ord, s + t)))


# [387] https://leetcode.com/problems/first-unique-character-in-a-string/
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# use find and rfind, x26 times
def firstUniqChar(s: str) -> int:
    alphabet = string.ascii_lowercase
    res = len(s)
    for x in alphabet:
        index = s.find(x)
        if index == -1:
            continue
        if index == s.rfind(x):
            res = min(res, index)
    return -1 if res == len(s) else res


# [205] https://leetcode.com/problems/isomorphic-strings/
# Given two strings s and t, determine if they are isomorphic.
#
# use dict
def isIsomorphic1(s: 'str', t: 'str') -> 'bool':
    if len(s) != len(t):
        return False

    char_dict = {}
    for c1, c2 in zip(s, t):
        if c1 in char_dict:
            if char_dict[c1] != c2:
                return False
        else:
            if c2 in char_dict.values():
                return False
            else:
                char_dict[c1] = c2
    return True


# use set
def isIsomorphic2(s: 'str', t: 'str') -> 'bool':
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))


# [249] https://leetcode.com/problems/group-shifted-strings/
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
#
# with defaultdict
def groupStrings(strings):
    groups = defaultdict(list)
    for s in strings:
        groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)] += s,  # += s, equals to append(s)
    return list(groups.values())


# with groupby
def groupStrings2(strings):
    key = lambda s: [(ord(c) - ord(s[0])) % 26 for c in s]
    return [list(g) for _, g in groupby(sorted(strings, key=key), key)]


# [290] https://leetcode.com/problems/word-pattern/
# Given a pattern and a string str, find if str follows the same pattern.
#
# use index
def wordPattern1(pattern, str):
    s = pattern
    t = str.split()
    return list(map(s.find, s)) == list(map(t.index, t))


# use set
def wordPattern2(pattern, str):
    s = pattern
    t = str.split()
    if len(s) != len(t):
        return False
    else:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


# [680] https://leetcode.com/problems/valid-palindrome-ii/
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
def validPalindrome(s):
    i = 0
    while i < len(s) // 2 and s[i] == s[~i]: i += 1
    s = s[i:len(s) - i]
    return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]


# [246] https://leetcode.com/problems/strobogrammatic-number/
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to determine if a number is strobogrammatic.
def isStrobogrammatic1(num):
    return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num) // 2 + 1))


def isStrobogrammatic2(num):
    return all(c + d in '696 00 11 88' for c, d in zip(num, num[::-1]))


def isStrobogrammatic3(num):
    return all(map('696 00 11 88'.count, map(operator.add, num, num[::-1])))


def isStrobogrammatic4(num):
    return set(map(operator.add, num, num[::-1])) <= {'69', '96', '00', '11', '88'}


# [247] https://leetcode.com/problems/strobogrammatic-number-ii/
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Find all strobogrammatic numbers that are of length = n.
def findStrobogrammatic1(n):
    nums = n % 2 * list('018') or ['']
    while n > 1:
        n -= 2
        # n < 2 is genius, to keep outside can not get 0
        nums = [a + num + b for a, b in '00 11 88 69 96'.split()[n < 2:] for num in nums]
    return nums


def findStrobogrammatic2(n):
    numbers = ['0', '1', '8'] if n % 2 else ['']
    for _ in range(n // 2):
        numbers = [head + s + tail for head, tail in [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
                   for s in numbers]
    return [s for s in numbers if s and (s[0] != '0' or len(s) == 1)]


# [345] https://leetcode.com/problems/reverse-vowels-of-a-string/
# Write a function that takes a string as input and reverse only the vowels of a string.
#
# use ~
def reverseVowels1(s: 'str') -> 'str':
    res = list(s)
    vowels_index = [i for i, c in enumerate(s) if c in 'aeiouAEIOU']
    for i in range(len(vowels_index) // 2):
        res[vowels_index[i]], res[vowels_index[~i]] = res[vowels_index[~i]], res[vowels_index[i]]
    return ''.join(res)


# use zip
def reverseVowels2(s: 'str') -> 'str':
    res = list(s)
    vowels_index = [i for i, c in enumerate(s) if c in 'aeiouAEIOU']
    half = len(vowels_index) // 2
    for i, j in zip(vowels_index[:half], vowels_index[-1:-half - 1:-1]):  # or vowels_index[half:][::-1]
        res[i], res[j] = res[j], res[i]
    return ''.join(res)


# [844] https://leetcode.com/problems/backspace-string-compare/
# Given two strings S and T, return if they are equal when both are typed into empty text editors.
#
# substring
def backspaceCompare1(S, T):
    back = lambda res, c: res[:-1] if c == '#' else res + c
    return reduce(back, S, "") == reduce(back, T, "")


# stack
def backspaceCompare2(S, T):
    def back(res, c):
        if c != '#':
            res.append(c)
        elif res:
            res.pop()
        return res

    return reduce(back, S, []) == reduce(back, T, [])


# O(1) Space
def backspaceCompare(S, T):
    i, j = len(S) - 1, len(T) - 1
    backS = backT = 0
    while True:
        while i >= 0 and (backS or S[i] == '#'):
            backS += 1 if S[i] == '#' else -1
            i -= 1
        while j >= 0 and (backT or T[j] == '#'):
            backT += 1 if T[j] == '#' else -1
            j -= 1
        if not (i >= 0 and j >= 0 and S[i] == T[j]):
            return i == j == -1
        i, j = i - 1, j - 1


# [165] https://leetcode.com/problems/compare-version-numbers/
# Compare two version numbers version1 and version2.
#
# pad with izip_longest with fillvalue=0
def compareVersion1(version1, version2):
    v1, v2 = map(int, version1.split('.')), map(int, version2.split('.'))
    v1, v2 = zip(*zip_longest(v1, v2, fillvalue=0))
    # cmp in python2
    return (v1 > v2) - (v1 < v2)


# pad with [0] * lengthDifference
def compareVersion2(version1, version2):
    v1, v2 = map(int, version1.split('.')), map(int, version2.split('.'))
    d = len(v2) - len(v1)
    v1, v2 = v1 + [0] * d, v2 + [0] * -d
    return (v1 > v2) - (v1 < v2)


# recursive, add zeros on the fly
def compareVersion3(version1, version2):
    main1, _, rest1 = ('0' + version1).partition('.')
    main2, _, rest2 = ('0' + version2).partition('.')
    return (int(main1) > int(main2)) - (int(main1) < int(main2)) or \
           len(rest1 + rest2) and compareVersion3(rest1, rest2)


# [38] https://leetcode.com/problems/count-and-say/
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
def countAndSay(n):
    result = '1'
    for _ in range(n - 1):
        prev = result
        result, j = '', 0
        while j < len(prev):
            cur = prev[j]
            cnt = 1
            j += 1
            while j < len(prev) and prev[j] == cur:
                cnt += 1
                j += 1
            result += str(cnt) + str(cur)
    return result


# [38] https://leetcode.com/problems/count-and-say/
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
#
# use groupby
def countAndSay2(n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + digit
                    for digit, group in groupby(s))
    return s


# [38] https://leetcode.com/problems/count-and-say/
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
#
# use regex
def countAndSay3(n):
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s


# [68] https://leetcode.com/problems/text-justification/
# Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
def fullJustify(words, maxWidth):
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i % (len(cur) - 1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(maxWidth)]


# [168] https://leetcode.com/problems/excel-sheet-column-title/
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
def convertToTitle(num):
    return "" if num == 0 else convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))


def convertToTitle2(num):
    capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    result = []
    while num > 0:
        result.append(capitals[(num - 1) % 26])
        num = (num - 1) // 26
    result.reverse()
    return ''.join(result)


# [171] https://leetcode.com/problems/excel-sheet-column-number/
# Given a column title as appear in an Excel sheet, return its corresponding column number.
def titleToNumber(s: str) -> int:
    return reduce(lambda x, y: x * 26 + y, [ord(c) - ord('A') + 1 for c in list(s)])


def titleToNumber1(s: 'str') -> 'int':
    base, res = 1, 0
    for c in s[::-1]:
        res += base * (ord(c) - ord('A') + 1)
        base *= 26
    return res


# [408] https://leetcode.com/problems/valid-word-abbreviation/
# Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.
def validWordAbbreviation(word: 'str', abbr: 'str') -> 'bool':
    i, n = 0, ''
    for c in abbr:
        if c.isalpha():
            # add '0' to compatible with n='' case
            i += int('0' + n)
            if i >= len(word) or c != word[i]:
                return False
            i, n = i + 1, ''
        else:
            n += c
            if n == '0':
                return False
    return i + int('0' + n) == len(word)


# regex
def validWordAbbreviation2(word, abbr):
    return bool(re.match(re.sub('([1-9]\d*)', r'.{\1}', abbr) + '$', word))


'''
application with string
'''


# [388] https://leetcode.com/problems/longest-absolute-file-path/
# Given a string representing the file system in the above format, return the length of the longest absolute path to
# file in the abstracted file system.
#
# use dict
def lengthLongestPath(input):
    maxlen = 0
    pathlen = {0: 0}
    for line in input.splitlines():
        # lstrip is better here
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth] + len(name))
        else:
            pathlen[depth + 1] = pathlen[depth] + len(name) + 1
    return maxlen


# [157] https://leetcode.com/problems/read-n-characters-given-read4/
# Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.
def read(buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Number of characters to read (int)
    :rtype: The number of actual characters read (int)
    """

    # fake api
    def read4(buf):
        pass

    idx = 0
    while n >= 4:
        read4_buf = [''] * 4
        read4(read4_buf)
        for i in range(4):
            buf[idx] = read4_buf[i]
            idx += 1
        n -= 4

    if n > 0:
        read4_buf = [''] * 4
        read4(read4_buf)
        for i in range(n):
            buf[idx] = read4_buf[i]
            idx += 1
    return idx


# [271] https://leetcode.com/problems/encode-and-decode-strings/
# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded back to the original list of strings.
class Codec:
    def encode(self, strs):
        return ''.join(s.replace('|', '||') + ' | ' for s in strs)

    def decode(self, s):
        return [t.replace('||', '|') for t in s.split(' | ')[:-1]]


# [418] https://leetcode.com/problems/sentence-screen-fitting/
# Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given
# sentence can be fitted on the screen.
#
# find pattern (simulator only in one big loop)
def wordsTyping1(sentence: 'List[str]', rows: int, cols: int) -> int:
    word_len = list(map(len, sentence))

    # try to find pattern, record result in every line
    line_count, firsts = [], [0]
    idx, count, condition = 0, 0, True
    remain = cols
    while condition:
        if remain >= word_len[idx]:
            remain -= word_len[idx] + 1
            idx = idx + 1
            if idx == len(word_len):
                count += 1
                idx = 0
        else:
            remain = cols
            line_count.append(count)

            # find it already
            if rows == len(line_count):
                return line_count[-1]

            # find a loop to exit
            for i, f in enumerate(firsts):
                if idx == f:
                    start = i
                    condition = False
                    break
            else:
                firsts.append(idx)

    c, r = divmod(rows - 1 - start, len(line_count) - start)
    repeat_count = line_count[-1] - (line_count[start - 1] if start > 0 else 0)
    return line_count[r + start] + c * repeat_count


# [418] https://leetcode.com/problems/sentence-screen-fitting/
# Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given
# sentence can be fitted on the screen.
#
# backtrack table
def wordsTyping2(words, rows, cols):
    sentence = " ".join(words) + ' '
    sentence_len = len(sentence)

    prev = -1
    backtrack = [0] * sentence_len
    for i in range(sentence_len):
        if sentence[i] == ' ':
            prev = i
        backtrack[i] = i - (prev + 1)

    pos = 0
    for _ in range(rows):
        pos += cols
        pos -= backtrack[pos % sentence_len]

    return (pos + 1) // sentence_len


# [722] https://leetcode.com/problems/remove-comments/
# Given a C++ program, remove comments from it.
#
# use regex
def removeComments1(source):
    return list(filter(None, re.sub('//.*|/\*(.|\n)*?\*/', '', '\n'.join(source)).split('\n')))


# parsing
def removeComments2(source):
    in_block = False
    res = []
    for line in source:
        i = 0
        if not in_block:
            newline = []
        while i < len(line):
            if line[i:i + 2] == '/*' and not in_block:
                in_block = True
                i += 1
            elif line[i:i + 2] == '*/' and in_block:
                in_block = False
                i += 1
            elif not in_block and line[i:i + 2] == '//':
                break
            elif not in_block:
                newline.append(line[i])
            i += 1
        if newline and not in_block:
            res.append("".join(newline))

    return res


# [681] https://leetcode.com/problems/next-closest-time/
# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
#
# Addition Simulator Solution
def nextClosestTime(time: str) -> str:
    words = sorted(list(set(time[:2] + time[3:])))
    res = list(time[:2] + time[3:])

    for idx in range(4)[::-1]:
        next_idx = words.index(res[idx]) + 1
        if next_idx < len(words):
            # change to the next digit
            res[idx] = words[next_idx]
            hour, minute = divmod(int(''.join(res)), 100)
            # if it is valid time, just return it
            if hour < 24 and minute < 60:
                return ''.join(res[:2]) + ':' + ''.join(res[2:])
        # back to the first digit, and carry to high-position
        res[idx] = words[0]
    return ''.join(res[:2]) + ':' + ''.join(res[2:])
