# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def trs_v2(nd,order,nullv,dd):
            #print(nd)
            if not nd:return [[nullv,dd]]
            elif not nd.left and not nd.right: res= [[nullv+[nd.val,'e'],dd+nd.val]]
            else:
                res= [[nullv+[nd.val],None]] + trs_v2(nd.left,order,nullv+[nd.val],dd+nd.val) + trs_v2(nd.right,order,nullv+[nd.val],dd+nd.val)
            return res        
        tli = trs_v2(root,'pre',[None],0)        
        print(tli)
        mli = [el[0] for el in tli if el[0][-1]=='e' and el[1]==targetSum] 
        mli = [[e for e in r if e is not None and e!='e'] for r in mli]
        print(mli)
        return mli if root and mli else [] 