# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def gt(left,right):
            #print(left,right)
            if (left,right) in cac:return cac[(left,right)]
            if left>right:return[]
            elif left==right:return [None]
            elif left+1==right: return [TreeNode(left)]
            res =[]
            
            for i in range(left,right):
                print('i=%s  %s~%s.><.%s~%s '%(i,left,i-1,i+1,right-1,))
               # print('i=%s  %s.><.%s left=%s riht=%s'%(i,left,right-1,len(gt(1,i)),len(gt(i+1,right))))
                for tdl in gt(left,i):
                    for tdr in gt(i+1,right):
                        td=TreeNode(i)
                        td.left=tdl
                        td.right=tdr
                        #if tdl or tdr: 
                        res.append(td)
            cac[(left,right)]=res
            return res
        cac={}
        return gt(1,n+1)