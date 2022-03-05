# [Count Complete Tree Nodes][title]

## Description

给你一棵 **完全二叉树** 的根节点 `root` ，求出该树的节点个数。

[完全二叉树](https://baike.baidu.com/item/%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91/7773232?fr=aladdin)
的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 `h`
层，则该层包含 `1~ 2h` 个节点。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/14/complete.jpg)
            **输入：** root = [1,2,3,4,5,6]    **输出：** 6    

**示例 2：**
            **输入：** root = []    **输出：** 0    

**示例 3：**
            **输入：** root = [1]    **输出：** 1    

**提示：**

  * 树中节点的数目范围是`[0, 5 * 104]`
  * `0 <= Node.val <= 5 * 104`
  * 题目数据保证输入的树是 **完全二叉树**

**进阶：** 遍历树来统计节点是一种时间复杂度为 `O(n)` 的简单解决方案。你可以设计一个更快的算法吗？


**Tags:** Tree, Depth-First Search, Binary Search, Binary Tree

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
    def countNodes(self, root: TreeNode) -> int:
        def midt(node):
            if not node: 
                tli.append(None)
            else:
                if node.left: midt(node.left)       
                tli.append(node.val)      
                if node.right: midt(node.right)  

        tli=[]   
        midt(root)
        return len(tli) if root else 0     
```

[title]: https://leetcode-cn.com/problems/count-complete-tree-nodes
