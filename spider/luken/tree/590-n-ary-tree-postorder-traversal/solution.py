"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def tr(nd):
            res = []
            for ch in nd.children:
                res += tr(ch)
            res +=[nd.val]
            return res
        if not root: return []
        tli = tr(root)
        print (tli)
        return tli        