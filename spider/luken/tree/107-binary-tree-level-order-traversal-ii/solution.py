# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        unt =1
        def trs_he(nd,order,nullv,dep):
            if not nd:return [[dep,nullv[0]]]
            elif not nd.left and not nd.right: res= [[dep*unt,nd.val]]
            else:
                res= [[dep,nd.val]] + trs_he(nd.left,order,nullv,dep+1) + trs_he(nd.right,order,nullv,dep+1)
            #print(nd,res)
            return res        

        tli = trs_he(root,'pre',[None],1)
        #print('...tli=%s'%tli)
        dic = {}
        for tt in tli:
            dic.setdefault(tt[0],[])
            if tt[1] is not None: dic[tt[0]].append(tt[1])
        if not root:return []
        return [xx[1] for xx in sorted(dic.items(),key=lambda xx:xx[0])][::-1]    