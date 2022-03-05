# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        def v2b(node):
            res,leaf,qpath,que=[[]],[],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                pa =   path+[node]
                que.append([node.left,h+1,pa])
                que.append([node.right,h+1,pa])  
                res[h].append(node)
            return res       
        res =v2b(root)
        if len(res)==2:return True
        print([[e.val for e in h] for h in res])
        full = [len(h) for h in res[1:-1]] == [2**i for i in range(len(res)-2)]
        if not full:return False
        print([len(h) for h in res[1:-1]])
        t= ''.join([['1','0'][ nd.left == None] +['1','0'][nd.right == None ]  for nd in res[-2]])
        print(t)
        while t and t[0]=='1': t=t[1:]
        return t.replace('0','')==''