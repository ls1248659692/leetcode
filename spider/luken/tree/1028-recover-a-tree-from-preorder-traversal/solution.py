# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def dtree_v1(s):
            nli = ['']
            for i in range(len(s)):
                if s[i] =='-' and s[i-1]!='-':
                    nli.append('-')
                else:
                    nli[-1] += s[i]
            return nli
        rg=lambda x,n:list(range(x,x+n))
        m4 = lambda md:[md,md-1,md,md]
        dt = dtree_v1(traversal)
        dt = [[el.count('-'),int(el.replace('-',''))]for el in dt]
        md= max([el[0]for el in dt])
        nli=[0]*md
        print('maxdepth.0->%sth nodenum=%s'%(md,len(dt)))

        root= TreeNode(dt[0][1])
        for i in range(1,len(dt)):
            depth,val=dt[i]
            for n in range(depth,md):nli[n]=0
            nli[depth-1]+=1
            print(val,depth,nli)
            node =root
            for dd in range(depth-1): node = node.left if nli[dd]%2  else node.right
            if nli[depth-1]%2 :node.left=TreeNode(val) 
            else: node.right=TreeNode(val)
        return root