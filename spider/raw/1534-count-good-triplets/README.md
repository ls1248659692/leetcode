# [Count Good Triplets][title]

## Description

给你一个整数数组 `arr` ，以及 `a`、`b` 、`c` 三个整数。请你统计其中好三元组的数量。

如果三元组 `(arr[i], arr[j], arr[k])` 满足下列全部条件，则认为它是一个 **好三元组** 。

  * `0 <= i < j < k < arr.length`
  * `|arr[i] - arr[j]| <= a`
  * `|arr[j] - arr[k]| <= b`
  * `|arr[i] - arr[k]| <= c`

其中 `|x|` 表示 `x` 的绝对值。

返回 **好三元组的数量** 。



**示例 1：**
            **输入：** arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3    **输出：** 4    **解释：** 一共有 4 个好三元组：[(3,0,1), (3,0,1), (3,1,1), (0,1,1)] 。    

**示例 2：**
            **输入：** arr = [1,1,2,2,3], a = 0, b = 0, c = 1    **输出：** 0    **解释：** 不存在满足所有条件的三元组。    



**提示：**

  * `3 <= arr.length <= 100`
  * `0 <= arr[i] <= 1000`
  * `0 <= a, b, c <= 1000`


**Tags:** Array, Enumeration

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = []
        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                for k in range(j+1,len(arr)):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c: res.append((arr[i],arr[j],arr[k]))
        return len(res)
```

[title]: https://leetcode-cn.com/problems/count-good-triplets
