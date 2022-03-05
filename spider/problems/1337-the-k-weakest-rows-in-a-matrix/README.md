# [The K Weakest Rows in a Matrix][title]

## Description

给你一个大小为 `m * n` 的矩阵 `mat`，矩阵由若干军人和平民组成，分别用 1 和 0 表示。

请你返回矩阵中战斗力最弱的 `k` 行的索引，按从最弱到最强排序。

如果第 _**i**_ 行的军人数量少于第 _**j**_ 行，或者两行军人数量相同但 _ **i**_ 小于 _**j**_ ，那么我们认为第 _
**i**_ 行的战斗力比第 _ **j**_ 行弱。

军人 **总是** 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。

**示例 1：**
            **输入：** mat =     [[1,1,0,0,0],     [1,1,1,1,0],     [1,0,0,0,0],     [1,1,0,0,0],     [1,1,1,1,1]],     k = 3    **输出：** [2,0,3]    **解释：**    每行中的军人数目：    行 0 -> 2     行 1 -> 4     行 2 -> 1     行 3 -> 2     行 4 -> 5     从最弱到最强对这些行排序后得到 [2,0,3,1,4]    

**示例 2：**
            **输入：** mat =     [[1,0,0,0],     [1,1,1,1],     [1,0,0,0],     [1,0,0,0]],     k = 2    **输出：** [0,2]    **解释：**     每行中的军人数目：    行 0 -> 1     行 1 -> 4     行 2 -> 1     行 3 -> 1     从最弱到最强对这些行排序后得到 [0,2,3,1]    

**提示：**

  * `m == mat.length`
  * `n == mat[i].length`
  * `2 <= n, m <= 100`
  * `1 <= k <= m`
  * `matrix[i][j]` 不是 0 就是 1


**Tags:** Array, Binary Search, Matrix, Sorting, Heap (Priority Queue)

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        li =[(sum(mat[i]),i) for i in range(len(mat))]
        return [e[1] for e in sorted(li,key=lambda x: x[0]*1000 + x[1])][:k]
```

[title]: https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix
