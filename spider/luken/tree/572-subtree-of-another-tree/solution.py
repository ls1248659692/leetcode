# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        tli =[]
        val = subRoot.val

        def se(nd):
            if nd.val== val:tli.append(nd)
            if nd.left:se(nd.left)
            if nd.right:se(nd.right)
        se(root)
    

        def pt(nd,nullval):
            if not nd:return nullval
            elif not nd.left and not nd.right: res= [ nd.val]
            else:res= [nd.val] + (pt(nd.left,nullval) if nd.left else nullval)+ (pt(nd.right,nullval) if nd.right else nullval)
            return res
        print(len(tli))
        #return False
        
        for subt in tli[::-1]:
            if pt(subt,[None])==pt(subRoot,[None]):return True
        return False