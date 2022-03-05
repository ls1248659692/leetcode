# [Partition Array Into Three Parts With Equal Sum][title]

## Description

给你一个整数数组 `arr`，只有可以将其划分为三个和相等的 **非空** 部分时才返回 `true`，否则返回 `false`。

形式上，如果可以找出索引 `i + 1 < j` 且满足 `(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] +
arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length -
1])` 就可以将数组三等分。

**示例 1：**
            **输入：** arr = [0,2,1,-6,6,-7,9,1,2,0,1]    **输出：** true    **解释：** 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1    

**示例 2：**
            **输入：** arr = [0,2,1,-6,6,7,9,-1,2,0,1]    **输出：** false    

**示例 3：**
            **输入：** arr = [3,3,6,5,-2,2,5,1,-9,4]    **输出：** true    **解释：** 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4    

**提示：**

  * `3 <= arr.length <= 5 * 104`
  * `-104 <= arr[i] <= 104`


**Tags:** Greedy, Array

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr)%3!=0:return False

        c =0
        s3= sum(arr)//3
        print(s3)
        cnt =0
        # b,e=100000,1000000
        for i in range(len(arr)-1):
            c+=arr[i]
            if c==s3:
                cnt+=1
                c =0
                # break

        # arr = arr[::-1]
        # c=0
        # for i in range(len(arr)):      
        #     c+=arr[i]
        #     if c==s3:
        #         e=i+1
        #         break
        # print(b,e)
        return  cnt>=2
```

[title]: https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum
