# [Check Completeness of a Binary Tree][title]

## Description

给定一个二叉树的 `root` ，确定它是否是一个  _完全二叉树_  。

在一个  **[完全二叉树](https://baike.baidu.com/item/完全二叉树/7773232?fr=aladdin)**
中，除了最后一个关卡外，所有关卡都是完全被填满的，并且最后一个关卡中的所有节点都是尽可能靠左的。它可以包含 `1` 到 `2h` 节点之间的最后一级 `h`
。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/12/15/complete-binary-tree-1.png)
            **输入：** root = [1,2,3,4,5,6]    **输出：** true    **解释：** 最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。    

**示例 2：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/12/15/complete-binary-tree-2.png)**
            **输入：** root = [1,2,3,4,5,null,7]    **输出：** false    **解释：** 值为 7 的结点没有尽可能靠向左侧。    



**提示：**

  * 树的结点数在范围  `[1, 100]` 内。
  * `1 <= Node.val <= 1000`


**Tags:** Tree, Breadth-First Search, Binary Tree

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
    def isCompleteTree(self, root: TreeNode) -> bool:
        def v2b(node):
            res,leaf,qpath,que=[[]],[],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                pa =   path+[node]
                que.append([node.left,h+1,pa])
                que.append([node.right,h+1,pa])  
                res[h].append(node)
            return res       
        res =v2b(root)
        if len(res)==2:return True
        print([[e.val for e in h] for h in res])
        full = [len(h) for h in res[1:-1]] == [2**i for i in range(len(res)-2)]
        if not full:return False
        print([len(h) for h in res[1:-1]])
        t= ''.join([['1','0'][ nd.left == None] +['1','0'][nd.right == None ]  for nd in res[-2]])
        print(t)
        while t and t[0]=='1': t=t[1:]
        return t.replace('0','')==''
```

[title]: https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree
