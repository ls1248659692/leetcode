# [Most Frequent Subtree Sum][title]

## Description

给你一个二叉树的根结点 `root` ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

一个结点的  **「子树元素和」**  定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/04/24/freq1-tree.jpg)
            **输入:** root = [5,2,-3]    **输出:** [2,-3,4]    

**示例  2：**

![](https://assets.leetcode.com/uploads/2021/04/24/freq2-tree.jpg)
            **输入:** root = [5,2,-5]    **输出:** [2]    



**提示:**

  * 节点数在 `[1, 104]` 范围内
  * `-105 <= Node.val <= 105`


**Tags:** Tree, Depth-First Search, Hash Table, Binary Tree

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
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def trs(node):
            if not node:r= None
            elif not node.left and not node.right:r= node.val
            else:
                lft,rht= trs(node.left),trs(node.right)
                r = (lft if lft else 0)+ (rht if rht else 0)+node.val
            if r is not None: d[r]=d.get(r,0)+1
            return r
        d={}
        trs(root)
        print(d)
        mx = max(list(d.values()))
        print(mx)
        return [k for k in d.keys() if d[k]==mx]
```

[title]: https://leetcode-cn.com/problems/most-frequent-subtree-sum
