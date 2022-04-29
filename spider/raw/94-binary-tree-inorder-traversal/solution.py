# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def v0(root):
            def midt(node):
                if not node: 
                    tli.append(None)
                else:
                    if node.left: midt(node.left)       
                    tli.append(node.val)      
                    if node.right: midt(node.right)  

            tli=[]   
            midt(root)
            return tli if root else []

        def v01(root):
            def midt(node,nullv):
                if not node: 
                    if nullv and nullv[0] is None: tli.append(None)
                else:
                    midt(node.left,nullv)       
                    tli.append(node.val)      
                    midt(node.right,nullv)  
            tli=[]   
            midt(root,[])
            return tli if root else []            

        def v1(node): 
            tli,stk=[],[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                #print([e.val for e in stk])
                node = stk.pop()
                tli.append(node.val)
                node = node.right 
            return tli        

        def v2(root):
            def p_nxt(path):
                while path and path[-1]=='1': path=path[:-1]
                return (path[:-1]+ {'0':'-','-':'1'}[path[-1]]) if path else ''

            def goto_nxtnd(root,pred):
                node,i = root,0
                pred_nxt = p_nxt(pred)
                print('p,pn',pred,pred_nxt)
                if not pred_nxt:return None,''
                while i<len(pred_nxt):
                    node =  {'0':node.left,'1':node.right,'-':node}[pred_nxt[i]]
                    if not node:
                        print('wish',pred_nxt)
                        if len(pred_nxt) == pred_nxt.count('1'):return None,''
                        pred_nxt = p_nxt(pred_nxt)
                        node,i=root,0
                        print('goto_ag',pred_nxt)
                        continue
                    i+=1
                print('return:',node.val,pred_nxt)
                return node,pred_nxt

            node = root 
            tli,pred,pred_nxt,par=[],'','',None
            while node:
                #print("check: '%s' , '%s'"%(pred,pred_nxt))
                while pred_nxt=='' and node.left :
                    pred+='0'
                    node = node.left  
                tli.append(node.val)
                pred_nxt=''
                print('rchk: pred %s val %s rval %s'%(pred,node.val,node.right.val if node.right else None))
                if node.right:
                    pred = pred.replace('-','')+'1'
                    node = node.right
                else:
                    node,pred_nxt= goto_nxtnd(root,pred)
                    if pred_nxt=='':break
                    pred = pred_nxt
                #print(tli,node.val,pred,pred_nxt)
            return tli

        def v2(nd):
            tls,stk=[],[]
            while nd or stk:
                while nd : 
                    stk.append(nd)
                    # tls.append(nd.val)
                    nd=nd.left
                nd=stk.pop()
                tls.append(nd.val)
                nd=nd.right
            return tls

        return v2(root) if root else []