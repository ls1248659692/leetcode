# [Flatten 2D Vector][title]

## Description

请设计并实现一个能够展开二维向量的迭代器。该迭代器需要支持 `next` 和 `hasNext` 两种操作。

**示例：**
            Vector2D iterator = new Vector2D([[1,2],[3],[4]]);        iterator.next(); // 返回 1    iterator.next(); // 返回 2    iterator.next(); // 返回 3    iterator.hasNext(); // 返回 true    iterator.hasNext(); // 返回 true    iterator.next(); // 返回 4    iterator.hasNext(); // 返回 false    

**注意：**

  1. 请记得 **重置** 在 Vector2D 中声明的类变量（静态变量），因为类变量会 **在多个测试用例中保持不变** ，影响判题准确。请 [查阅](https://support.leetcode-cn.com/hc/kb/section/1071534/) 这里。
  2. 你可以假定 `next()` 的调用总是合法的，即当 `next()` 被调用时，二维向量总是存在至少一个后续元素。

**进阶：** 尝试在代码中仅使用 [C++
提供的迭代器](http://www.cplusplus.com/reference/iterator/iterator/) 或 [Java
提供的迭代器](https://docs.oracle.com/javase/7/docs/api/java/util/Iterator.html)。


**Tags:** Design, Array, Two Pointers, Iterator

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/flatten-2d-vector
