# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def trs_v2(nd,order,nullv,dd):
            #print(nd)
            if not nd:return [[nullv,dd]]
            elif not nd.left and not nd.right: res= [[nullv+[nd.val,'e'],dd+nd.val]]
            else:
                res= [[nullv+[nd.val],None]] + trs_v2(nd.left,order,nullv+[nd.val],dd+nd.val) + trs_v2(nd.right,order,nullv+[nd.val],dd+nd.val)
            return res        
        tli = trs_v2(root,'pre',[None],0)        
        print(tli)
        mli = [el[0] for el in tli if el[0][-1]=='e' ] 
        mli = [''.join([str(e) for e in r if e is not None and e!='e']) for r in mli]
        su = sum([int(e) for e in mli])
        print(mli)
        return su        