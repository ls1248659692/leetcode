# [Count Good Nodes in Binary Tree][title]

## Description

给你一棵根为 `root` 的二叉树，请你返回二叉树中好节点的数目。

「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。



**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/05/16/test_sample_1.png)**
            **输入：** root = [3,1,4,3,null,1,5]    **输出：** 4    **解释：** 图中蓝色节点为好节点。    根节点 (3) 永远是个好节点。    节点 4 -> (3,4) 是路径中的最大值。    节点 5 -> (3,4,5) 是路径中的最大值。    节点 3 -> (3,1,3) 是路径中的最大值。

**示例 2：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/05/16/test_sample_2.png)**
            **输入：** root = [3,3,null,4,2]    **输出：** 3    **解释：** 节点 2 -> (3, 3, 2) 不是好节点，因为 "3" 比它大。

**示例 3：**
            **输入：** root = [1]    **输出：** 1    **解释：** 根节点是好节点。



**提示：**

  * 二叉树中节点数目范围是 `[1, 10^5]` 。
  * 每个节点权值的范围是 `[-10^4, 10^4]` 。


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
    def goodNodes(self, root: TreeNode) -> int:
        def v2(node):
            res,leaf,que=[[[node.val]]],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                pathb =path+[node]
                que.append([node.left,h+1,pathb])
                que.append([node.right,h+1,pathb])  
                res[h].append(pathb)
                if not node.right and not node.left:
                    leaf.append(pathb)
            print([[nd.val for nd in pa] for pa in leaf])
            return leaf
        leaf= v2(root) 
        ndset =set()
        for pa in leaf:
            ndset.add(pa[0])
            mx= pa[0].val
            for i in range(1,len(pa)):
                if pa[i].val>=mx:
                    ndset.add(pa[i])
                    mx =pa[i].val
        return len(ndset)
                   
```

[title]: https://leetcode-cn.com/problems/count-good-nodes-in-binary-tree
