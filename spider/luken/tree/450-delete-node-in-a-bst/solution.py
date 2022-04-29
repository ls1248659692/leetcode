# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def v1(node,key):
            root,par, match = node,None,False
            while node and node.val!=key:
                
                if key<node.val: par,node=node,node.left
                else: par,node=node,node.right
            if node and key == node.val:match=True
            if not match: return root
            prv,nxn= node.left,node.right
            #node.left,node.right =None,None
            if par is not None:
                cd = 'L' if par.left==node else 'R'
                if nxn is not None:
                    if prv is None:
                        if cd=='R':par.right=nxn
                        if cd=='L':par.left=nxn
                    else:
                        link= prv
                        while link.right: link= link.right
                        link.right =nxn
                        if cd=='R': par.right=prv
                        if cd=='L': par.left=prv
                else:
                    if cd=='R': par.right=prv
                    if cd=='L': par.left=prv
            else:
                if nxn is not None:
                    if  prv is None:
                        return nxn
                    else:
                        lnk = nxn
                        while lnk.left: lnk= lnk.left
                        lnk.left =prv
                        return nxn
                else:
                    return prv                
            return root 

        return v1(root,key) if root else None