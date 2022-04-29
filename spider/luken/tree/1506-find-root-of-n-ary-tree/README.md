# [Find Root of N-Ary Tree][title]

## Description

给定一棵 [N 叉树](https://slack-
redir.net/link?url=https%3A%2F%2Fleetcode.com%2Farticles%2Fintroduction-to-n-
ary-trees) 的所有节点在一个数组 `Node[] tree` 中，树中每个节点都有 **唯一的值** 。

找到并返回 N 叉树的 **根节点** 。

**自定义测试：**

_N 叉树的输入序列为其层序遍历序列，每组子节点用 null 分隔（见示例）。_

_![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/07/21/sample_4_964.png)_

上图中的 N 叉树的序列化描述为
`[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`
。

**测试将以下列方式进行：**

  * 输入数据的形式为树的序列化描述。
  * 驱动程序代码将根据序列化的输入数据构造树，并以任意顺序将每个 `Node` 对象放入一个数组中。
  * 驱动程序代码将把数组传递给 `findRoot` ，你所编写的函数应该在数组中查找并返回根 `Node` 对象。
  * 驱动程序代码将接受返回的 `Node` 对象并对其进行序列化。如果序列化的结果和输入数据 **相同** ，则测试 **通过** 。

**示例 1：**

![](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)
            **输入：** tree = [1,null,3,2,4,null,5,6]    **输出：** [1,null,3,2,4,null,5,6]    **解释：** 来自输入数据的树如上所示。    驱动程序代码创建树，并以任意顺序向 findRoot 提供 Node 对象。    例如，传递的数组可以是 [Node(5),Node(4),Node(3),Node(6),Node(2),Node(1)] 或 [Node(2),Node(6),Node(1),Node(3),Node(5),Node(4)] 。    findRoot 函数应该返回根 Node(1) ，驱动程序代码将序列化它并与输入数据进行比较。    输入数据和序列化的 Node(1) 相同，因此测试通过。

**示例 2：**

![](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)
            **输入：** tree = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]    **输出：** [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]    

**提示：**

  * 节点的总个数在 `[1, 5*10^4]` 之间。
  * 每个节点都有唯一的值。

**进阶：**

  * 你可以使用 O(1) 额外内存空间且 O(n) 时间复杂度的算法来找到该树的根节点吗？


**Tags:** Bit Manipulation, Tree, Depth-First Search, Hash Table

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/find-root-of-n-ary-tree
