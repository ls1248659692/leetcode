# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        pre,pos= preorder,postorder
        v= lambda x: x.val if x else None
        def cpp(low,upp,pol,pou):
            if low+1>upp:return 
            if low+1==upp: 
                td2=TreeNode(pre[low])
                print('td2',v(td2),pre[low:upp],pos[pol:pou],1)
            elif low+2==upp: 
                td2=TreeNode(pre[low]) 
                td2.left=TreeNode(pre[low+1])  
                print('td2',v(td2),pre[low:upp],pos[pol:pou],2)      
            else:
                td2 = TreeNode(pre[low])
                lfti=pos[pol:pou].index(pre[low+1]) 
                print('td2',v(td2),pre[low:upp],pos[pol:pou],lfti)
                td2.left=cpp(low+1,low+lfti+2,pol,pol+lfti+1)
                td2.right=cpp(low+lfti+2,upp,pol+lfti+1,pou-1)
                
            return td2
        
        return cpp(0,len(pre),0,len(pos))        