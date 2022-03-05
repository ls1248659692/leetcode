# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def v2(node):
            res,que=[['.']],[[node,1,'-']]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                que.append([node.left,h+1,path+'L'])
                que.append([node.right,h+1,path+'R'])  
                res[h].append(path+':'+str(node.val))
            return res #[:-1] if len(res)>=2 else res
        r=  v2(root)
        print(r,len(r))
        ht= len(r)-1
        g=[['']*(2**ht-1) for i in range(ht)]
        print(g)
        for i in range(1,len(r)):
            for nd in r[i]:
                path,val = nd.split(':')
                path = path.replace('L','0').replace('R','1').replace('-','')
                #print(path)
                if not path: 
                    t= (int('0',base=2)*2**(ht+1-i)+ 2**(ht-i)-1)  #1
                else:
                    t=int(path,base=2)*2**(ht+1-i)+ 2**(ht-i)-1
                print(t)
                if val:g[i-1][t]=val
                    # if i==2:print(int(path,base=2)*2**(ht+1-i)+ 2**(ht-i)-1)
                    # if i==3: print(int(path,base=2)*2**(ht+1-i)+ 2**(ht-i)-1)
                    # if i==4: print('h4',int(path,base=2)*2**(ht+1-i)+ 2**(ht-i)-1)
                #print(t,val)
        return g