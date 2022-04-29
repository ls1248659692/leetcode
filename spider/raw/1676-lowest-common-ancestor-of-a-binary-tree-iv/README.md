# [Lowest Common Ancestor of a Binary Tree IV][title]

## Description

给定一棵二叉树的根节点 `root` 和 `TreeNode` 类对象的数组（列表） `nodes`，返回 __`nodes`
中所有节点的最近公共祖先（LCA）。数组（列表）中所有节点都存在于该二叉树中，且二叉树中所有节点的值都是互不相同的。

我们扩展[二叉树的最近公共祖先节点在维基百科上的定义](https://en.wikipedia.org/wiki/Lowest_common_ancestor)：“对于任意合理的
`i` 值， `n` 个节点 `p1` 、 `p2`、...、 `pn` 在二叉树 `T` 中的最近公共祖先节点是 **后代** 中包含所有节点 `pi`
的最深节点（我们允许一个节点是其自身的后代）”。一个节点 `x` 的后代节点是节点 `x` 到某一叶节点间的路径中的节点 `y`。

**示例 1:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
            **输入:** root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]    **输出:** 2    **解释:** 节点 4 和 7 的最近公共祖先是 2。    

**示例 2:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
            **输入:** root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]    **输出:** 1    **解释:** 单个节点的最近公共祖先是该节点本身。        

**示例 3:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
            **输入:** root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]    **输出:** 5    **解释:** 节点 7、6、2 和 4 的最近公共祖先节点是 5。    

**示例 4:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
            **输入:** root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [0,1,2,3,4,5,6,7,8]    **输出:** 3    **解释:** 树中所有节点的最近公共祖先是根节点。    

**提示:**

  * 树中节点个数的范围是 `[1, 104]` 。
  * `-109 <= Node.val <= 109`
  * 所有的 `Node.val` 都是 **互不相同** 的。
  * 所有的 `nodes[i]` 都存在于该树中。
  * 所有的 `nodes[i]` 都是互不相同的。


**Tags:** Tree, Depth-First Search, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree-iv
