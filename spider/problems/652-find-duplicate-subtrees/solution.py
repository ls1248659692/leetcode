# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def search(node):
            nli,res,nres,stk=set(),[],[],[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                node = stk.pop()
                nd_s = serial(node)
                for q in nli:
                    if nd_s==q:
                       if q not in nres:
                           res.append(node)
                           nres.append(nd_s)
                       break
                nli.add(nd_s)
                node = node.right 
            return res

        def serial(node):
            def midt(node):
                if not node: 
                    tli.append('#')
                else:
                    tli.append(str(node.val)) 
                    midt(node.left)      
                    midt(node.right)  
            tli=[]   
            midt(node)
            print(','.join(tli))
            return ','.join(tli) if node else ''
        # return serial(root)
        return search(root)               