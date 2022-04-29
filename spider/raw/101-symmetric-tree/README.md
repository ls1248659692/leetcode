# [Symmetric Tree][title]

## Description

给你一个二叉树的根节点 `root` ， 检查它是否轴对称。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)
            **输入：** root = [1,2,2,3,4,4,3]    **输出：** true    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)
            **输入：** root = [1,2,2,null,3,null,3]    **输出：** false    



**提示：**

  * 树中节点数目在范围 `[1, 1000]` 内
  * `-100 <= Node.val <= 100`



**进阶：** 你可以运用递归和迭代两种方法解决这个问题吗？


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

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
    def __init__(self):
        self.tli=[]

    def l_midtr(self,root):
        if not root: return self.tli
        if not root.left and not root.right:
            self.tli.append(root.val)
            return self.tli
        if root.left:
            self.l_midtr(root.left)
        else:
            self.tli.append(None)
            #return
        
        if root.right:
            self.l_midtr(root.right)
        else:
            self.tli.append(None)
            #return            
        self.tli.append(root.val)
        return self.tli

    def r_midtr(self,root):
        if not root: return self.tli
        if not root.left and not root.right:
            self.tli.append(root.val)
            return self.tli
        if root.right:
            self.r_midtr(root.right)
        else:
            self.tli.append(None)
            #return               
        
        if root.left:
            self.r_midtr(root.left)
        else:
            self.tli.append(None)
            #return     
        self.tli.append(root.val)    
        return self.tli

    def isSymmetric_v0(self, root: TreeNode) -> bool:
        self.l_midtr(root.left)
        print(self.tli)
        l_tr=list(self.tli)
        print('l_tr=',l_tr)
        self.tli=[]
        self.r_midtr(root.right)
        r_tr=list(self.tli)
        print('r_tr=',r_tr)

        return l_tr ==r_tr

    def isSymmetric_v1(self, root: TreeNode) -> bool:
        def midtr( root,tli,firstc):
            if not root: tli.append(None)
            elif not root.left and not root.right: tli.append(root.val)
            else:  
                f,s = (root.left,root.right) if firstc=='L' else (root.right,root.left)
                midtr(f,tli,firstc)
                midtr(s,tli,firstc)
                tli.append(root.val)

        ltli,rtli = [],[]
        midtr(root.left,ltli,'L')
        midtr(root.right,rtli,'R')
        return ltli == rtli


    def isSymmetric(self, root: TreeNode) -> bool:        
        def compare(left, right):
            if None in [left,right]: return left==right
            elif left.val != right.val: return False
            return compare(left.left, right.right) and compare(left.right, right.left) 
        
        return compare(root.left, root.right) if root else True
```

[title]: https://leetcode-cn.com/problems/symmetric-tree
