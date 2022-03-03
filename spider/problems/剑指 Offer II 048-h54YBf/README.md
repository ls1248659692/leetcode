# [序列化与反序列化二叉树][title]

## Description

序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 /
反序列化算法执行逻辑，只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)
            **输入：** root = [1,2,3,null,null,4,5]    **输出：** [1,2,3,null,null,4,5]    

**示例 2：**
            **输入：** root = []    **输出：** []    

**示例 3：**
            **输入：** root = [1]    **输出：** [1]    

**示例 4：**
            **输入：** root = [1,2]    **输出：** [1,2]    



**提示：**

  * 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 [LeetCode 序列化二叉树的格式](/faq/#binary-tree)。你并非必须采取这种方式，也可以采用其他的方法解决这个问题。
  * 树中结点数在范围 `[0, 104]` 内
  * `-1000 <= Node.val <= 1000`



注意：本题与主站 297 题相同：<https://leetcode-cn.com/problems/serialize-and-deserialize-
binary-tree/>


**Tags:** Tree, Depth-First Search, Breadth-First Search, Design, String, Binary Tree

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/h54YBf
