# [Trim a Binary Search Tree][title]

## Description

给你二叉搜索树的根节点 `root` ，同时给定最小边界`low` 和最大边界 `high`。通过修剪二叉搜索树，使得所有节点的值在`[low,
high]`中。修剪树 **不应该**  改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在
**唯一的答案**  。

所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/09/trim1.jpg)
            **输入：** root = [1,0,2], low = 1, high = 2    **输出：** [1,null,2]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/09/09/trim2.jpg)
            **输入：** root = [3,0,4,null,2,null,null,1], low = 1, high = 3    **输出：** [3,2,null,1]    



**提示：**

  * 树中节点数在范围 `[1, 104]` 内
  * `0 <= Node.val <= 104`
  * 树中每个节点的值都是 **唯一** 的
  * 题目数据保证输入是一棵有效的二叉搜索树
  * `0 <= low <= high <= 104`


**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

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
```

[title]: https://leetcode-cn.com/problems/trim-a-binary-search-tree
