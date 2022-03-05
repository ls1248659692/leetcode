"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        dli =[[]]
        def dp(nd,hr):
            if len(dli)<=hr :dli.append([])
            dli[hr].append(nd.val)
            for ch in nd.children:
                dp(ch,hr+1)

        if not root:return 0
        dp(root,1)
        print(len(dli))
        return len(dli)-1