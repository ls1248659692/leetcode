# [二叉搜索树中两个节点之和][title]

## Description

给定一个二叉搜索树的 **根节点** `root` 和一个整数 `k` , 请判断该二叉搜索树中是否存在两个节点它们的值之和等于 `k`
。假设二叉搜索树中节点的值均唯一。



**示例 1：**
            **输入:** root = **** [8,6,10,5,7,9,11], k = 12    **输出:** true    **解释:** 节点 5 和节点 7 之和等于 12    

**示例 2：**
            **输入:** root = **** [8,6,10,5,7,9,11], k = 22    **输出:** false    **解释:** 不存在两个节点值之和为 22 的节点    



**提示：**

  * 二叉树的节点个数的范围是  `[1, 104]`.
  * `-104 <= Node.val <= 104`
  * `root` 为二叉搜索树
  * `-105 <= k <= 105`



注意：本题与主站 653 题相同： <https://leetcode-cn.com/problems/two-sum-iv-input-is-a-
bst/>


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
    def findTarget(self, root: TreeNode, k: int) -> bool:
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

[title]: https://leetcode-cn.com/problems/opLdQZ
