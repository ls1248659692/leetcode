# [Unique Binary Search Trees II][title]

## Description

给你一个整数 `n` ，请你生成并返回所有由 `n` 个节点组成且节点值从 `1` 到 `n` 互不相同的不同 **二叉搜索树** __ 。可以按
**任意顺序** 返回答案。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg)
            **输入：** n = 3    **输出：** [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]    

**示例 2：**
            **输入：** n = 1    **输出：** [[1]]    

**提示：**

  * `1 <= n <= 8`


**Tags:** Tree, Binary Search Tree, Dynamic Programming, Backtracking, Binary Tree

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
    def generateTrees(self, n: int) -> List[TreeNode]:

        def gt(left,right):
            #print(left,right)
            if (left,right) in cac:return cac[(left,right)]
            if left>right:return[]
            elif left==right:return [None]
            elif left+1==right: return [TreeNode(left)]
            res =[]
            
            for i in range(left,right):
                print('i=%s  %s~%s.><.%s~%s '%(i,left,i-1,i+1,right-1,))
               # print('i=%s  %s.><.%s left=%s riht=%s'%(i,left,right-1,len(gt(1,i)),len(gt(i+1,right))))
                for tdl in gt(left,i):
                    for tdr in gt(i+1,right):
                        td=TreeNode(i)
                        td.left=tdl
                        td.right=tdr
                        #if tdl or tdr: 
                        res.append(td)
            cac[(left,right)]=res
            return res
        cac={}
        return gt(1,n+1)
```

[title]: https://leetcode-cn.com/problems/unique-binary-search-trees-ii
