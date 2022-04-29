# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        def v2b(node):
            res,leaf,que=[[[node]]],[],[[node,1,None,'-']]
            while que:
                node,h,par,pd =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                que.append([node.left,h+1, node, 'L'])
                que.append([node.right,h+1,node,'R'])  
                pa =  path+[node]
                res[h].append([node,par,pd])
                if not node.right and not node.left: leaf.append(pa)
            return res

        res= v2b(root)   
        print('len_r=%s'%len(res))
        print([[e[0].val for e in h] for h in res[1:]])
        tli=[]
        if depth==1:
            td= TreeNode(val)
            td.left=root
            return td
        elif depth == len(res):
            for nd,par,pd in res[depth-1]:
                td = TreeNode(val)
                tli.append(td)
                nd.left=td
                td = TreeNode(val)
                tli.append(td)                
                nd.right=td
            return root            
        else:
            for nd,par,pd in res[depth-1]:
                td = TreeNode(val)
                tli.append([td,nd,'L'])
                nd.left=td
                td = TreeNode(val)
                tli.append([td,nd,'R'])                
                nd.right=td

            for nd,par,pd in res[depth]:
                for td_,par_,pd_ in tli:
                    if par==par_ and pd_==pd:
                        if pd=='L':
                            td_.left = nd
                        else:
                            td_.right=nd
                        break

            return root