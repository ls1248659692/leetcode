# [Three in One LCCI][title]

## Description

三合一。描述如何只用一个数组来实现三个栈。

你应该实现`push(stackNum,
value)`、`pop(stackNum)`、`isEmpty(stackNum)`、`peek(stackNum)`方法。`stackNum`表示栈下标，`value`表示压入的值。

构造函数会传入一个`stackSize`参数，代表每个栈的大小。

**示例1:**
            **输入** ：    ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]    [[1], [0, 1], [0, 2], [0], [0], [0], [0]]    **输出** ：    [null, null, null, 1, -1, -1, true]    **说明** ：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。    

**示例2:**
            **输入** ：    ["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]    [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]    **输出** ：    [null, null, null, null, 2, 1, -1, -1]    



**提示：**

  * `0 <= stackNum <= 2`


**Tags:** Stack, Design, Array

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/three-in-one-lcci
