# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def singledir(x,dir):
            if len(x)==1: return {'upp':x[0]%2==1,'dwn':x[0]%2==0}[dir]
            for i in range(1,len(x)): 
                if dir =='upp':
                    if x[i]<=x[i-1] or x[i]%2==0 or x[i-1]%2==0: return False
                if dir =='dwn':
                    if x[i]>=x[i-1] or x[i]%2==1 or x[i-1]%2==1: return False
            return True

        def v1(node):
            res,que=[[node.val]],[[node,1]]
            while que:
                node,h =que.pop(0)
                while h>=len(res):res.append([])
                if node.left: 
                    res[h].append(node.left.val)
                    que.append([node.left,h+1])
                if node.right:
                    res[h].append(node.right.val)
                    que.append([node.right,h+1])  
            return res[:-1]        


        r=v1(root)
        print (r)
        return sum(not singledir(r[i], 'upp' if i%2==0 else 'dwn') for i in range(len(r))) == 0