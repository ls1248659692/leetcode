# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def v1(node): 
            tls,stk=[],[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                #print([e.val for e in stk])
                node = stk.pop()
                tls.append(node)
                node = node.right 
            return tls     
        tls=v1(root)   
        vls=[e.val for e in tls]
        print(vls)
        clst,c=[0]*len(vls),0
        for i in range(len(vls)-1,-1,-1): c,clst[i]=c+vls[i],c+vls[i]
        print(clst)
        for i in range(len(tls)):tls[i].val=clst[i]
        return root
            