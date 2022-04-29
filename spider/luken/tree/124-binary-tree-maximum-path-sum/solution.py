# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def tr(nd):
            if not nd:res= [[-99999,-99999,-99999,-99999]]
            elif not nd.right and not nd.left: res= [nd.val,nd.val,nd.val,nd.val] # val,max_D,max_norootD,max_leftR,max_rightR
            else:
                if nd.left and nd.right:
                    lf,ri = tr(nd.left),tr(nd.right)
                    # res = [nd.val, max(lf[-3],ri[-3],max(lf[-2:]+[0])+nd.val+max(ri[-2:]+[0])),max(lf[-2:]+[0])+nd.val,max(ri[-2:]+[0])+nd.val]
                    res = [nd.val, max(lf[-4:]+ri[-4:]),max(lf[-2:]+[0])+nd.val,max(ri[-2:]+[0])+nd.val]
                    res.insert(1,max(res[1:]+[res[-1]+res[-2]-nd.val]))
                elif nd.left:
                    lf,ri = tr(nd.left),[None]
                    res = [nd.val, max(lf[-4:]+[-99999]),max(lf[-2:]+[0])+nd.val,-99999]
                    res.insert(1,max(res[1:]+[res[-1]+res[-2]-nd.val]))
                elif nd.right:
                    lf,ri = [None],tr(nd.right)
                    res = [nd.val, max(ri[-4:]+[-99999]),-99999,max(ri[-2:]+[0])+nd.val]   
                    res.insert(1,max(res[1:]+[res[-1]+res[-2]-nd.val]))
            print('nd=%s,res=%s'%(nd.val,res))         
            return res    
        tli = tr(root)   
        print('tli=%s'%tli)
        return max(tli[1:]+[tli[-1]+tli[-2]-root.val])