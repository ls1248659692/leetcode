# [Maximum Level Sum of a Binary Tree][title]

## Description

给你一个二叉树的根节点 `root`。设根节点位于二叉树的第 `1` 层，而根节点的子节点位于第 `2` 层，依此类推。

请返回层内元素之和 **最大** 的那几层（可能只有一层）的层号，并返回其中  **最小** 的那个。



**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/08/17/capture.jpeg)**
            **输入：** root = [1,7,0,7,-8,null,null]    **输出：** 2    **解释：**    第 1 层各元素之和为 1，    第 2 层各元素之和为 7 + 0 = 7，    第 3 层各元素之和为 7 + -8 = -1，    所以我们返回第 2 层的层号，它的层内元素之和最大。    

**示例 2：**
            **输入：** root = [989,null,10250,98693,-89388,null,null,null,-32127]    **输出：** 2    



**提示：**

  * 树中的节点数在 `[1, 104]`范围内
  * `-105 <= Node.val <= 105`


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def v2(node):
            res,leaf,que=[[]],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                pathb =path+[node.val]
                que.append([node.left,h+1,pathb])
                que.append([node.right,h+1,pathb])  
                res[h].append(node.val)
                if not node.right and not node.left:
                    leaf.append(pathb)
            #print(leaf)
            return res

        r=v2(root) 
        print(r)
        sr = [sum(h) for h in r]
        mx= max(sr[1:])
        return [i for i in range(len(r)) if sr[i]==mx][0]
```

[title]: https://leetcode-cn.com/problems/maximum-level-sum-of-a-binary-tree
