# [Lowest Common Ancestor of a Binary Tree][title]

## Description

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

[百度百科](https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin)中最近公共祖先的定义为：“对于有根树
T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（ **一个节点也可以是它自己的祖先** ）。”

**示例 1：**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
            **输入：** root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1    **输出：** 3    **解释：** 节点 5 和节点 1 的最近公共祖先是节点 3 。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
            **输入：** root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4    **输出：** 5    **解释：** 节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。    

**示例 3：**
            **输入：** root = [1,2], p = 1, q = 2    **输出：** 1    

**提示：**

  * 树中节点数目在范围 `[2, 105]` 内。
  * `-109 <= Node.val <= 109`
  * 所有 `Node.val` `互不相同` 。
  * `p != q`
  * `p` 和 `q` 均存在于给定的二叉树中。


**Tags:** Tree, Depth-First Search, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def v2(node,p,q):
            trv,mat,que=[[[node]]],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(trv):trv.append([])
                que.append([node.left,h+1,path+[node]])
                que.append([node.right,h+1,path+[node]])  
                pa = path+[node,TreeNode('end')] if not node.right and not node.left else  path+[node]
                #trv[h].append(pa)
                if node in (p,q):
                    mat.append(pa)
            #print([[e.val for e in r] for r in mat])
            return mat

        mat= v2(root,p,q)  
        m0,m1 = (mat[1],mat[0]) if len(mat[0])> len(mat[1]) else (mat[0],mat[1])
        shr=m0[0]
        for i in range(len(m0)):
            if m0[i]==m1[i]:shr=m0[i]
        return shr
        
```

[title]: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
