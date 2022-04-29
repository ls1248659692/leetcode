# [Sum of Left Leaves][title]

## Description

给定二叉树的根节点 `root` ，返回所有左叶子之和。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg)
            **输入:** root = [3,9,20,null,null,15,7]     **输出:** 24     **解释:** 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24    

**示例  2:**
            **输入:** root = [1]    **输出:** 0    



**提示:**

  * 节点数在 `[1, 1000]` 范围内
  * `-1000 <= Node.val <= 1000`




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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        unit = 1
        sm = []

        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[dd]]
            elif not nd.left and not nd.right: 
                res= [[nd.val]+[dd*unit]]
                if order=='left': sm.append(nd.val)
            else:
                res= [[nd.val]+[dd]] + trs(nd.left,'left',nullv,dd+1) + trs(nd.right,'right',nullv,dd+1)
            return res        
        tli = trs(root,'root',[None],1)  
        print(sum(sm))
        return sum(sm)      
```

[title]: https://leetcode-cn.com/problems/sum-of-left-leaves
