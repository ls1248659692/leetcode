from collections import defaultdict
from functools import reduce


# [872] https://leetcode.com/problems/leaf-similar-trees/
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
def leafSimilar(root1, root2):
    def dfs(root, seq):
        if not root.left and not root.right:
            seq.append(root.val)

        if root.left:
            dfs(root.left, seq)

        if root.right:
            dfs(root.right, seq)

    seq1, seq2 = [], []
    dfs(root1, seq1)
    dfs(root2, seq2)
    return seq1 == seq2


# [339] https://leetcode.com/problems/nested-list-weight-sum/
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
def depthSum(nestedList: 'List[NestedInteger]') -> int:
    def dfs(depth, nested_list):
        res = 0
        for ni in nested_list:
            if ni.isInteger():
                res += depth * ni.getInteger()
            else:
                res += dfs(depth + 1, ni.getList())
        return res

    return dfs(1, nestedList)


# [47] https://leetcode.com/problems/permutations-ii/
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
def permuteUnique(nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            # all the index to insert
            for i in range(len(l) + 1):
                new_ans.append(l[:i] + [n] + l[i:])
                # handles duplication
                if i < len(l) and l[i] == n:
                    break
        ans = new_ans
    return ans


def permuteUnique2(nums):
    return reduce(lambda perms, n: [p[:i] + [n] + p[i:] for p in perms for i in range((p + [n]).index(n) + 1)], nums, [[]])


# [282] https://leetcode.com/problems/expression-add-operators/
# return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
def addOperators(num, target):
    res = []

    def dfs(num, temp, cur, last, res):
        if not num:
            if cur == target:
                res.append(temp)
            return

        for i in range(1, len(num) + 1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
                dfs(num[i:], temp + "+" + val, cur + int(val), int(val), res)
                dfs(num[i:], temp + "-" + val, cur - int(val), -int(val), res)
                dfs(num[i:], temp + "*" + val, cur - last + last * int(val), last * int(val),
                    res)  # revert add and multiply first

    for i in range(1, len(num) + 1):
        if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
            dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)  # this step put first number in the string
    return res


# [851] https://leetcode.com/problems/loud-and-rich/
# return answer, where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of
# quiet[y]), among all people who definitely have equal to or more money than person x.
def loudAndRich(richer, quiet):
    m = defaultdict(list)
    for i, j in richer:
        m[j].append(i)
    res = [-1] * len(quiet)

    def dfs(i):
        if res[i] >= 0:
            return res[i]
        res[i] = i
        for j in m[i]:
            if quiet[res[i]] > quiet[dfs(j)]:
                res[i] = res[j]
        return res[i]

    for i in range(len(quiet)):
        dfs(i)
    return res
