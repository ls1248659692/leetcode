# [Find Mode in Binary Search Tree][title]

## Description

给你一个含重复值的二叉搜索树（BST）的根节点 `root` ，找出并返回 BST 中的所有
[众数](https://baike.baidu.com/item/%E4%BC%97%E6%95%B0/44796)（即，出现频率最高的元素）。

如果树中有不止一个众数，可以按 **任意顺序** 返回。

假定 BST 满足如下定义：

  * 结点左子树中所含节点的值 **小于等于** 当前节点的值
  * 结点右子树中所含节点的值 **大于等于** 当前节点的值
  * 左子树和右子树都是二叉搜索树



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg)
            **输入：** root = [1,null,2,2]    **输出：** [2]    

**示例 2：**
            **输入：** root = [0]    **输出：** [0]    



**提示：**

  * 树中节点的数目在范围 `[1, 104]` 内
  * `-105 <= Node.val <= 105`



**进阶：** 你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）


**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

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
    def findMode(self, root: TreeNode) -> List[int]:
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
        nli = [tt[0] for tt in tli]
        ctli = [(n,nli.count(n)) for n in set(nli)]     
        print(ctli)   
        maxct = max(el[1] for el in ctli)
        return [el[0] for el in ctli if el[1]==maxct]
```

[title]: https://leetcode-cn.com/problems/find-mode-in-binary-search-tree
