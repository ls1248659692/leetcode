# [Two Sum IV - Input is a BST][title]

## Description

给定一个二叉搜索树 `root` 和一个目标结果 `k`，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 `true`。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg)
            **输入:** root = [5,3,6,2,4,null,7], k = 9    **输出:** true    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg)
            **输入:** root = [5,3,6,2,4,null,7], k = 28    **输出:** false    



**提示:**

  * 二叉树的节点个数的范围是  `[1, 104]`.
  * `-104 <= Node.val <= 104`
  * `root` 为二叉搜索树
  * `-105 <= k <= 105`


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Hash Table, Two Pointers, Binary Tree

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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[order]+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val,order]+[dd*unit]]
            else:
                res=  trs(nd.left,'r%d'%nd.val,nullv,dd+1) +[[nd.val,order]+[dd]]+ trs(nd.right,'r%d'%nd.val,nullv,dd+1)
            return res        
        tli = trs(root,'r%d'%root.val,[None],1) 
        nli = [el[0] for el in tli if el[0] is not None]
        for i in range(len(nli)):
            if k-nli[i] in nli[i+1:]:return True
        return False
```

[title]: https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst
