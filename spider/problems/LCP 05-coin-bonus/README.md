# [Coin Bonus][title]

## Description

力扣决定给一个刷题团队发`LeetCoin`作为奖励。同时，为了监控给大家发了多少`LeetCoin`，力扣有时候也会进行查询。



该刷题团队的管理模式可以用一棵树表示：

  1. 团队只有一个负责人，编号为1。除了该负责人外，每个人有且仅有一个领导（负责人没有领导）；
  2. 不存在循环管理的情况，如A管理B，B管理C，C管理A。



力扣想进行的操作有以下三种：

  1. 给团队的一个成员（也可以是负责人）发一定数量的`LeetCoin`；
  2. 给团队的一个成员（也可以是负责人），以及他/她管理的所有人（即他/她的下属、他/她下属的下属，……），发一定数量的`LeetCoin`；
  3. 查询某一个成员（也可以是负责人），以及他/她管理的所有人被发到的`LeetCoin`之和。



**输入：**

  1. `N`表示团队成员的个数（编号为1～N，负责人为1）；
  2. `leadership`是大小为`(N - 1) * 2`的二维数组，其中每个元素`[a, b]`代表`b`是`a`的下属；
  3. `operations`是一个长度为`Q`的二维数组，代表以时间排序的操作，格式如下：     1. `operations[i][0] = 1`: 代表第一种操作，`operations[i][1]`代表成员的编号，`operations[i][2]`代表`LeetCoin`的数量；    2. `operations[i][0] = 2`: 代表第二种操作，`operations[i][1]`代表成员的编号，`operations[i][2]`代表`LeetCoin`的数量；    3. `operations[i][0] = 3`: 代表第三种操作，`operations[i][1]`代表成员的编号；

**输出：**

返回一个数组，数组里是每次 **查询**
的返回值（发`LeetCoin`的操作不需要任何返回值）。由于发的`LeetCoin`很多，请把每次查询的结果模`1e9+7 (1000000007)`。



**示例 1：**
            **输入：** N = 6, leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]], operations = [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]    **输出：** [650, 665]    **解释：** 团队的管理关系见下图。    第一次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 0;    第二次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 15.    

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/09/09/coin_example_1.jpg)



**限制：**

  1. `1 <= N <= 50000`
  2. `1 <= Q <= 50000`
  3. `operations[i][0] != 3 时，1 <= operations[i][2] <= 5000`


**Tags:** Binary Indexed Tree, Segment Tree, Array

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/coin-bonus
