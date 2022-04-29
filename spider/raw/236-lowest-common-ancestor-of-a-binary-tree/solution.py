# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def v2(node,p,q):
            trv,mat,que=[[[node]]],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(trv):trv.append([])
                que.append([node.left,h+1,path+[node]])
                que.append([node.right,h+1,path+[node]])  
                pa = path+[node,TreeNode('end')] if not node.right and not node.left else  path+[node]
                #trv[h].append(pa)
                if node in (p,q):
                    mat.append(pa)
            #print([[e.val for e in r] for r in mat])
            return mat

        mat= v2(root,p,q)  
        m0,m1 = (mat[1],mat[0]) if len(mat[0])> len(mat[1]) else (mat[0],mat[1])
        shr=m0[0]
        for i in range(len(m0)):
            if m0[i]==m1[i]:shr=m0[i]
        return shr
        