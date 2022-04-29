# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def v0(root):
            singledir = lambda x:  sum(1 for i in range(1,len(x)) if x[i]-x[i-1]<=0)==0
            def midt(node):
                if not node: 
                    tli.append(None)
                else:
                    if node.left: midt(node.left)       
                    tli.append(node)      
                    if node.right: midt(node.right)  

            tli=[]   
            midt(root)     
            trli = [e for e in tli if e is not None] 
            vvli = [e.val for e in tli if e is not None] 
            sn = sorted(vvli)
            badi=[i for i in range(len(vvli)) if vvli[i]!=sn[i]]
            a,b=badi[:2]
            trli[b].val,trli[a].val=trli[a].val,trli[b].val
            #return root
            print(vvli)
        v0(root)        