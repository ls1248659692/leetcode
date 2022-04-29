# [Longest Turbulent Subarray][title]

## Description

给定一个整数数组 `arr` ，返回 `arr` 的  _最大湍流子数组的 **长度**_ ** ** 。

如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是  **湍流子数组**  。

更正式地来说，当 `arr` 的子数组 `A[i], A[i+1], ..., A[j]` 满足仅满足下列条件时，我们称其为 _湍流子数组_ ：

  * 若 `i <= k < j` ：     * 当 `k` 为奇数时， `A[k] > A[k+1]`，且    * 当 `k` 为偶数时，`A[k] < A[k+1]`；
  * **或** 若 `i <= k < j` ：     * 当 `k` 为偶数时，`A[k] > A[k+1]` ，且    * 当 `k` 为奇数时， `A[k] < A[k+1]`。



**示例 1：**
            **输入：** arr = [9,4,2,10,7,8,8,1,9]    **输出：** 5    **解释：** arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

**示例 2：**
            **输入：** arr = [4,8,12,16]    **输出：** 2    

**示例 3：**
            **输入：** arr = [100]    **输出：** 1    



**提示：**

  * `1 <= arr.length <= 4 * 104`
  * `0 <= arr[i] <= 109`


**Tags:** Array, Dynamic Programming, Sliding Window

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)<=1:return len(arr)
        dif = [arr[i]-arr[i-1] for i in range(1,len(arr))]
        print(dif)
        if set(dif)==set([0]):return 1
        c,r,mx=dif[0],1,1
        for i in range(1,len(dif)):
            if c*dif[i]<0: 
                r+=1
                if mx<r:mx=r
            else:
                r=1
            c=dif[i]
            
        return mx+1


```

[title]: https://leetcode-cn.com/problems/longest-turbulent-subarray
