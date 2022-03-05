# [Clone N-ary Tree][title]

## Description

给定一棵 N 叉树的根节点 `root` ，返回该树的[
**深拷贝**](https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin)（克隆）。

N 叉树的每个节点都包含一个值（ `int` ）和子节点的列表（ `List[Node]` ）。
            class Node {        public int val;        public List<Node> children;    }    

_N 叉树的输入序列用层序遍历表示，每组子节点用 null 分隔（见示例）。_



**示例 1：**

![](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)
            **输入：** root = [1,null,3,2,4,null,5,6]    **输出：** [1,null,3,2,4,null,5,6]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)
            **输入：** root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]    **输出：** [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]    



**提示：**

  * 给定的 N 叉树的深度小于或等于 `1000`。
  * 节点的总个数在 `[0, 10^4]` 之间



**进阶：** 你的解决方案可以适用于[克隆图](https://leetcode-cn.com/problems/clone-graph/)问题吗？


**Tags:** Tree, Depth-First Search, Breadth-First Search, Hash Table

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/clone-n-ary-tree
