# [Number of Ways to Build House of Cards][title]

## Description

You are given an integer `n` representing the number of playing cards you
have. A **house of cards** meets the following conditions:

  * A **house of cards** consists of one or more rows of **triangles** and horizontal cards.
  * **Triangles** are created by leaning two cards against each other.
  * One card must be placed horizontally between **all adjacent** triangles in a row.
  * Any triangle on a row higher than the first must be placed on a horizontal card from the previous row.
  * Each triangle is placed in the **leftmost** available spot in the row.

Return _the number of **distinct** **house of cards** you can build using
**all**_ `n` _cards._ Two houses of cards are considered distinct if there
exists a row where the two houses contain a different number of cards.



**Example 1:**

![](https://assets.leetcode.com/uploads/2022/02/27/image-20220227213243-1.png)
            Input: n = 16    Output: 2    Explanation: The two valid houses of cards are shown.    The third house of cards in the diagram is not valid because the rightmost triangle on the top row is not placed on top of a horizontal card.    

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/02/27/image-20220227213306-2.png)
            Input: n = 2    Output: 1    Explanation: The one valid house of cards is shown.    

**Example 3:**

![](https://assets.leetcode.com/uploads/2022/02/27/image-20220227213331-3.png)
            Input: n = 4    Output: 0    Explanation: The three houses of cards in the diagram are not valid.    The first house of cards needs a horizontal card placed between the two triangles.    The second house of cards uses 5 cards.    The third house of cards uses 2 cards.    



**Constraints:**

  * `1 <= n <= 500`


**Tags:** Math, Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/number-of-ways-to-build-house-of-cards
