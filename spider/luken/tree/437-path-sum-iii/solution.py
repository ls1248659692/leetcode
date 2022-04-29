# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def sumsubtg(ar,target):
            ln,pa = len(ar),set()
            for i in range(ln):
                c=ar[i]
                if c==target:pa.add(','.join([str(e)for e in ar[:i+1]]))
                for j in range(i+1,ln):
                    c+=ar[j]
                    if c==target:pa.add(','.join([str(e)for e in ar[:j+1]]))
            return pa

        def v1(root):
            def trs_v2(nd,order,nullv,dd):
                #print(nd)
                if not nd:return [[nullv,dd]]
                elif not nd.left and not nd.right: res= [[nullv+[nd.val,'e'],dd+nd.val]]
                else:
                    res= [[nullv+[nd.val],None]] + trs_v2(nd.left,order,nullv+[nd.val],dd+nd.val) + trs_v2(nd.right,order,nullv+[nd.val],dd+nd.val)
                return res        
            tli = trs_v2(root,'pre',[None],0)        
            #print(tli)
            mli = [el[0] for el in tli if el[0][-1]=='e' ] 
            #mli = [''.join([str(e) for e in r if e is not None and e!='e']) for r in mli]
            mli = [ [e for e in r if e is not None and e!='e'] for r in mli]
            print(mli)
            ss = set()
            for r in mli:
                ss = ss|sumsubtg(r,targetSum)
            print(ss)
            return len(ss)

        def v2(node,targetSum):
            res,leaf,que,cnt=[[[node.val]]],[],[[node,1,[]]],0
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                que.append([node.left,h+1,path+[node.val]])
                que.append([node.right,h+1,path+[node.val]])  
                pa = path+[node.val]
                res[h].append(pa)
                cum=0
                for j in range(len(pa)-1,-1,-1):
                    cum += pa[j]
                    if cum==targetSum:cnt+=1
            return cnt
        return v2(root,targetSum) if root else 0