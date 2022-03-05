# [House Robber III][title]

## Description

小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 `root` 。

除了 `root` 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果
**两个直接相连的房子在同一天晚上被打劫** ，房屋将自动报警。

给定二叉树的 `root` 。返回  _ **在不触动警报的情况下**  ，小偷能够盗取的最高金额_ 。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/03/10/rob1-tree.jpg)
            **输入:** root = [3,2,3,null,3,null,1]    **输出:** 7     **解释:**  小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7

**示例 2:**

![](https://assets.leetcode.com/uploads/2021/03/10/rob2-tree.jpg)
            **输入:** root = [3,4,5,1,3,null,1]    **输出:** 9    **解释:**  小偷一晚能够盗取的最高金额 4 + 5 = 9    



**提示：**

  * 树的节点数在 `[1, 104]` 范围内
  * `0 <= Node.val <= 104`


**Tags:** Tree, Depth-First Search, Dynamic Programming, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
# Definition for a binary tree nd.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def f(nd):
            if nd in cache: return cache[nd]
            if nd is None :return 0
            f1= f(nd.left)+f(nd.right)
            f2= (f(nd.left.left)+f(nd.left.right) if nd.left else 0) +(f(nd.right.left)+f(nd.right.right) if nd.right else 0)+nd.val
            res= max(f1,f2)
            cache[nd]=res
            return res
        cache={}
        return f(root)
```

[title]: https://leetcode-cn.com/problems/house-robber-iii
