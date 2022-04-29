# [Diameter of Binary Tree][title]

## Description

给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。



**示例 :**  
给定二叉树
                      1             / \            2   3           / \               4   5        

返回  **3** , 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。



**注意：** 两结点之间的路径长度是以它们之间边的数目表示。


**Tags:** Tree, Depth-First Search, Binary Tree

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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def tr(nd):
            if not nd:res= [[0,0,0,0]]
            elif not nd.right and not nd.left: res= [[nd.val,0,0,0]] # val,max_both,max_left,max_right
            else:
                if nd.left and nd.right:
                    lft,rht = tr(nd.left),tr(nd.right)
                    lf,ri = lft[-1],rht[-1]
                    res = lft+ rht + [[nd.val, max(lf[-3],ri[-3],max(lf[-2:])+2+max(ri[-2:])),max(lf[-2:])+1,max(ri[-2:])+1]]
                elif nd.left:
                    lft,rht = tr(nd.left),[None]
                    lf,ri = lft[-1],rht[-1]
                    res = lft +  [[nd.val, max(lf[-3],0),max(lf[-2:])+1,0]]
                elif nd.right:
                    lft,rht = [None],tr(nd.right)
                    lf,ri = lft[-1],rht[-1]
                    res = rht +  [[nd.val, max(ri[-3],0),0,max(ri[-2:])+1]       ]   
            #print('nd=%s,res=%s'%(nd,res))         
            return res    
        tli = tr(root)   
        print('tli=%s'%tli)
        return max(tli[-1][-3:])
```

[title]: https://leetcode-cn.com/problems/diameter-of-binary-tree
