# [Binary Searchable Numbers in an Unsorted Array][title]

## Description

有一个 **类似** [二分搜索](https://leetcode.com/explore/learn/card/binary-search/)的方法。
这个方法有两个入参: `sequence` 是一个整数数组， `target` 是一个整数。 这个方法可以判断 `target` 是否存在
`sequence`中。

该方法的伪代码如下：
            func(sequence, target)      while sequence is not empty        **randomly** choose an element from sequence as the pivot        if pivot = target, return **true**        else if pivot < target, remove pivot and all elements to its left from the sequence        else, remove pivot and all elements to its right from the sequence      end while      return **false**

当 `sequence` 是排好序时, 这个方法对 **所有** 值都可正常判断。如果 `sequence` 不是排好序的,
该方法并不是对所有值都可正常判断, 但对 **一些** 值仍可正常判断。

给定一个仅包含 **不同** 数字的数组 `nums`表示 `sequence`， nums **是否排序未知** ，对于 **所有可能** 的选择,
返回通过这个方法 **保证** 能找到的值的数量。



**示例  1:**
            **输入:** nums = [7]    **输出:** 1    **解释** :     7 保证能被找到.    因为数组中只有一个数字, 7 一定会被选中. 因为选中的值等于target, 这个方法会返回 true.    

**示例  2:**
            **输入:** nums = [-1,5,2]    **输出:** 1    **解释** :     只有 -1 保证能被找到.    如果 -1 被选中, 这个方法就会返回 true.    如果 5 被选中, 5 和 2 会被移除。 在下一次循环时, 这个序列只有一个元素： -1 ，这个方法就会返回 true.    如果 2 被选中, 2 将会被移除。 在下次循环时, 这个序列里将会有 -1 和 5. 无论哪个数字被选中, 这个方法都会找到 -1 且返回 true.        5 不能保证被找到。    如果 2 被选中, -1, 5 和 2 将会被移除。 这个序列将会被清空且这个方法会返回 false。        2 不能保证被找到.    如果 5 被选中, 5 和 2 将会被移除。在下次循环时, 这个序列只会有一个元素： -1 且这个方法会返回 false。        因为只有-1 是保证能被找到的, 你应该返回 1.    



**提示:**

  * `1 <= nums.length <= 105`
  * `-105 <= nums[i] <= 105`
  * `nums` 中所有值都  **不同**.



**提升:**  如果 `nums` 存在  **重复的值** , 你会如何修改你的算法吗?


**Tags:** 

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/binary-searchable-numbers-in-an-unsorted-array
