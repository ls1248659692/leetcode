# [Longest Common Subsequence Between Sorted Arrays][title]

## Description

给定一个由整数数组组成的数组`arrays`，其中`arrays[i]`是严格递增排序的，返回一个表示所有数组之间的最长公共子序列的整数数组。

子序列是从另一个序列派生出来的序列，删除一些元素或不删除任何元素，而不改变其余元素的顺序。

**示例1:**
            **输入:** arrays = [[ ** _1_** ,3, ** _4_** ],                   [ ** _1_** , ** _4_** ,7,9]]    **输出:** [1,4]    **解释:** 这两个数组中的最长子序列是[1,4]。    

**示例 2:**
            **输入:** arrays = [[ ** _2_** , ** _3_** , ** _6_** ,8],                   [1, ** _2_** , ** _3_** ,5, ** _6_** ,7,10],                   [ ** _2_** , ** _3_** ,4, _ **6**_ ,9]]    **输出:** [2,3,6]    **解释:** 这三个数组中的最长子序列是[2,3,6]。    

**示例 3:**
            **输入:** arrays = [[1,2,3,4,5],                   [6,7,8]]    **输出:** []    **解释:** 这两个数组之间没有公共子序列。    

**限制条件:**

  * `2 <= arrays.length <= 100`
  * `1 <= arrays[i].length <= 100`
  * `1 <= arrays[i][j] <= 100`
  * `arrays[i]` 是严格递增排序.


**Tags:** Array, Hash Table, Counting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/longest-common-subsequence-between-sorted-arrays
