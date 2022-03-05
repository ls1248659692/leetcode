# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def v2b(node,q=None,endh=float('inf'),ex=[]):
            res,leaf,qpath,que=[[]],[],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                if h>endh+1:break

                while h>=len(res):res.append([])
                pa =   path+[node]

                if q and node ==q:
                    qpath=list(pa)
                elif node not in ex:               
                    que.append([node.left,h+1,pa])
                    que.append([node.right,h+1,pa])  
                    res[h].append(node.val)
            print(res)
            return res[endh+1:] if endh<100 else res,qpath
        # æå±éåï¼ åè®¾tg å¨j , if j<=k, else j>k
        r,qpath = v2b(root,target)
        print('r=%s q=%s len=%s'%(r,[e.val for e in qpath],len(qpath)))

        tli,qlen = [],len(qpath)

        for i in range(qlen-1,-1,-1):
            if k-(qlen-1-i)<0:break
            nd =qpath[i]
            print('nd.val=%s,i=%s kk=%s'%(nd.val, i,k-qlen+1))
            res,_p = v2b(nd,endh=k) if i==qlen-1 else  v2b(nd,endh=k-(qlen-1-i),ex=[qpath[i+1]]) 
            print(res)
            tli+= [e for e in res[-1]] if res else []
        return tli