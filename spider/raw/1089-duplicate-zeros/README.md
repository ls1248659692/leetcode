# [Duplicate Zeros][title]

## Description

给你一个长度固定的整数数组 `arr`，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

注意：请不要在超过该数组长度的位置写入元素。

要求：请对输入的数组  **就地  **进行上述修改，不要从函数返回任何东西。



**示例 1：**
            **输入：** [1,0,2,3,0,4,5,0]    **输出：** null    **解释：** 调用函数后， **输入** 的数组将被修改为：[1,0,0,2,3,0,0,4]    

**示例 2：**
            **输入：** [1,2,3]    **输出：** null    **解释：** 调用函数后， **输入** 的数组将被修改为：[1,2,3]    



**提示：**

  1. `1 <= arr.length <= 10000`
  2. `0 <= arr[i] <= 9`


**Tags:** Array, Two Pointers

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        la_i=0
        zn=0
        for i in range(len(arr)-1,-1,-1):
            if arr[i]!=0 and la_i==0:
                la_i = i
            if la_i and arr[i]==0:
                zn+=1
        print(la_i,zn)
        for i in range(la_i,-1,-1):
            if arr[i]!=0:
                if i+zn <len(arr):arr[i+zn]= arr[i]
            else:
                if i+zn <len(arr):arr[i+zn]=0
                zn -=1
                if i+zn <len(arr):arr[i+zn]=0
        
        
        
```

[title]: https://leetcode-cn.com/problems/duplicate-zeros
