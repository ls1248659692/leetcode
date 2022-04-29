# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def v1(node):
            res,que=[['0']],[[node,1,'0']]
            while que:
                node,h,path =que.pop(0)
                while h>=len(res):res.append([])
                if node.left: 
                    res[h].append(path+'0')
                    que.append([node.left,h+1,path+'0'])
                if node.right:
                    res[h].append(path+'1')
                    que.append([node.right,h+1,path+'1'])  
            print(res)
            pos=[int(r[-1],base=2)-int(r[0],base=2)+1 for r in res[:-1]]
            print(pos) 
            return max(pos)

        return v1(root)             