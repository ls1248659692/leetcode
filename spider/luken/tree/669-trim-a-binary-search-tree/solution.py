# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def tt(nd,v,t):
            nonlocal par,direct,root
            while nd :
                if nd.val==v:
                    if t=='mi': nd.left=None
                    else: nd.right=None
                    break
                elif nd.val<v:
                    if t=='mi': 
                        if direct=='L': par.left=nd.right
                        if direct=='R': par.right=nd.right 
                        if direct=='': root= nd.right   
                        par,direct,nd= par,direct,nd.right
                    else:                
                        par,direct,nd= nd,'R',nd.right                    
                elif nd.val>v: 
                    if t=='mx': 
                        if direct=='L': par.left=nd.left
                        if direct=='R': par.right=nd.left  
                        if direct=='': root= nd.left     
                        par,direct,nd= par,direct,nd.left
                    else:                         
                        par,direct,nd =nd,'L',nd.left

            print(nd,par.val if par else None)
        par,direct=None,''
        tt(root,low,'mi')
        par,direct=None,''
        tt(root,high,'mx')        
        return root