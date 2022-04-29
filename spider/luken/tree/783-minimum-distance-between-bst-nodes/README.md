# [Minimum Distance Between BST Nodes][title]

## Description

给你一个二叉搜索树的根节点 `root` ，返回 **树中任意两不同节点值之间的最小差值** 。

差值是一个正数，其数值等于两值之差的绝对值。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg)
            **输入：** root = [4,2,6,1,3]    **输出：** 1    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg)
            **输入：** root = [1,0,48,null,null,12,49]    **输出：** 1    



**提示：**

  * 树中节点的数目范围是 `[2, 100]`
  * `0 <= Node.val <= 105`



**注意：** 本题与 530：<https://leetcode-cn.com/problems/minimum-absolute-difference-
in-bst/> 相同


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree

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
    def minDiffInBST(self, root: TreeNode) -> int:
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[order]+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val,order]+[dd*unit]]
            else:
                res= [[nd.val,order]+[dd]] + trs(nd.left,'r%d'%nd.val,nullv,dd+1) + trs(nd.right,'r%d'%nd.val,nullv,dd+1)
            return res        
        tli = trs(root,'r%d'%root.val,[None],1) 
        print(tli)       
        tli = [tt for tt in tli if tt[0] is not None]
        nli = [tt[0] for tt in sorted(tli,key=lambda xx:xx[0])]
        return min (abs(nli[i]-nli[i+1]) for i in range(len(nli)-1))        
```

[title]: https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes
