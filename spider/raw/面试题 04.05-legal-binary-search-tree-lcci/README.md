# [Legal Binary Search Tree LCCI][title]

## Description

实现一个函数，检查一棵二叉树是否为二叉搜索树。

 **示例 1:**
             **输入:**          2         / \        1   3       **输出:** true      

 **示例 2:**
             **输入:**          5         / \        1   4           / \          3   6       **输出:** false       **解释:** 输入为: [5,1,4,null,null,3,6]。           根节点的值为 5 ，但是其右子节点值为 4 。


**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def v0(root):
            def rol(l,o,r):
                if l is None and r is None :return [o,o]
                if r is None: return [l,o] if l<o else [None,None]
                if l is None: return [o,r] if o<r else [None,None]
                return [l,r] if l<o<r else [None,None]

            def isv(nd):
                if tli:return [None,None]
                if not nd:return []
                if not nd.left and not nd.right:return [nd.val,nd.val]
                lft = isv(nd.left)
                if lft and lft[0] is None: tli.append(False)  
                rht = isv(nd.right)
                if rht and rht[0] is None:  tli.append(False)
                print(lft,nd.val,rht)
                tmp = rol(lft[1] if lft else None,nd.val,rht[0] if rht else None)
                print('tmp=%s'%tmp)
                if tmp[0] is None: tli.append(False)
                return lft[0] if lft else nd.val, rht[1] if rht else nd.val
            tli=[]
            isv(root)
            return False if tli else True

        def v1(root):
            def isv(nd,l=FMI,r=FMX):
                if not nd:return True
                #if True or nd.left is None and nd.right is None:
                #    print('leaf',nd.val,l,r)
                #    return True if l<nd.val<r else False
                if True or nd.left :
                    #print('lf',nd.left.val,l,nd.val)
                    if not isv(nd.left,l=l,r=nd.val) : return False
                        
                if True or nd.right :
                    #print('rt',nd.right.val,nd.val,r)
                    if not isv(nd.right,l=nd.val,r=r) :return False
                        
                return l<nd.val<r
            return isv(root)

        def v3(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not v3(node.right, val, upper):
                return False
            if not v3(node.left, lower, val):
                return False
            return True

        

        FMI,FMX= float('-inf'),float('inf')
        if not root:return True
        return True if v1(root) else False
        return v3(root)


```

[title]: https://leetcode-cn.com/problems/legal-binary-search-tree-lcci
