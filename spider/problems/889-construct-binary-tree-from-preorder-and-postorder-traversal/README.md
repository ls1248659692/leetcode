# [Construct Binary Tree from Preorder and Postorder Traversal][title]

## Description

给定两个整数数组，`preorder` 和 `postorder` ，其中 `preorder` 是一个具有 **无重复**
值的二叉树的前序遍历，`postorder` 是同一棵树的后序遍历，重构并返回二叉树。

如果存在多个答案，您可以返回其中 **任何** 一个。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/07/24/lc-prepost.jpg)
            **输入：** preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]    **输出：** [1,2,3,4,5,6,7]    

**示例 2:**
            **输入:** preorder = [1], postorder = [1]    **输出:** [1]    



**提示：**

  * `1 <= preorder.length <= 30`
  * `1 <= preorder[i] <= preorder.length`
  * `preorder` 中所有值都 **不同**
  * `postorder.length == preorder.length`
  * `1 <= postorder[i] <= postorder.length`
  * `postorder` 中所有值都 **不同**
  * 保证 `preorder` 和 `postorder` 是同一棵二叉树的前序遍历和后序遍历


**Tags:** Tree, Array, Hash Table, Divide and Conquer, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
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
```

[title]: https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal
