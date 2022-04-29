"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def v1(node):
            res,que=[[node.val]],[[node,1]]
            while que:
                node,h =que.pop(0)
                while len(res)<=h:res.append([])
                for ch in node.children:
                    res[h].append(ch.val)
                    que.append([ch,h+1])
            return res[:-1]         
        return v1(root) if root else []