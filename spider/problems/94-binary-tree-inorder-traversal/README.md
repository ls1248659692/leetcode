# [Binary Tree Inorder Traversal][title]

## Description

给定一个二叉树的根节点 `root` ，返回它的 **中序** 遍历。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)
            **输入：** root = [1,null,2,3]    **输出：** [1,3,2]    

**示例 2：**
            **输入：** root = []    **输出：** []    

**示例 3：**
            **输入：** root = [1]    **输出：** [1]    

**示例 4：**

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg)
            **输入：** root = [1,2]    **输出：** [2,1]    

**示例 5：**

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg)
            **输入：** root = [1,null,2]    **输出：** [1,2]    

**提示：**

  * 树中节点数目在范围 `[0, 100]` 内
  * `-100 <= Node.val <= 100`

**进阶:** 递归算法很简单，你可以通过迭代算法完成吗？


**Tags:** Stack, Tree, Depth-First Search, Binary Tree

**Difficulty:** Easy

## 思路

``` python3
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
```

[title]: https://leetcode-cn.com/problems/binary-tree-inorder-traversal
