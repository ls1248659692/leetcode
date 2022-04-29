# [二叉树染色][title]

## Description

小扣有一个根结点为 `root` 的二叉树模型，初始所有结点均为白色，可以用蓝色染料给模型结点染色，模型的每个结点有一个 `val`
价值。小扣出于美观考虑，希望最后二叉树上每个蓝色相连部分的结点个数不能超过 `k` 个，求所有染成蓝色的结点价值总和最大是多少？ **示例 1：** >
输入：`root = [5,2,3,4], k = 2` > > 输出：`12` > > 解释：`结点 5、3、4 染成蓝色，获得最大的价值
5+3+4=12` ![image.png](https://pic.leetcode-cn.com/1616126267-BqaCRj-
image.png) **示例 2：** > 输入：`root = [4,1,3,9,null,null,2], k = 2` > > 输出：`16` >
> 解释：结点 4、3、9 染成蓝色，获得最大的价值 4+3+9=16 ![image.png](https://pic.leetcode-
cn.com/1616126301-gJbhba-image.png) **提示：** \+ `1 <= k <= 10` \+ `1 <= val <=
10000` \+ `1 <= 结点数量 <= 10000`


**Tags:** Tree, Dynamic Programming, Binary Tree

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/er-cha-shu-ran-se-UGC
