# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def v0(root):
            singledir = lambda x:  sum(1 for i in range(1,len(x)) if x[i]-x[i-1]<=0)==0
            def midt(node):
                if not node: 
                    tli.append(None)
                else:
                    if node.left: midt(node.left)       
                    tli.append(node.val)      
                    if node.right: midt(node.right)  

            tli=[]   
            midt(root)     
            tli = [e for e in tli if e is not None] 
            return singledir(tli)

        def v1(root):
            def check(node):
                if not node:pass
                else:
                    chkl,chkr,v={},{},node.val
                    if not node.left and not node.right: return {'st':True,'v':[v]}
                    if node.left:
                        chkl = check(node.left)
                        if not chkl['st'] or not chkl['v'][-1]<v: return {'st':False,'v':[v]}
                    if node.right:
                        chkr=check(node.right)
                        if not chkr['st'] or not v<chkr['v'][0]:return {'st':False,'v':[v]}
                    return {'st':True,'v':[chkl['v'][0] if chkl else v,chkr['v'][-1] if chkr else v,]}
            return check(root)['st']
        return v1(root)
