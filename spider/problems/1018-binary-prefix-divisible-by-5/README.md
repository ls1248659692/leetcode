# [Binary Prefix Divisible By 5][title]

## Description

给定由若干 `0` 和 `1` 组成的数组 `A`。我们定义 `N_i`：从 `A[0]` 到 `A[i]` 的第 `i`
个子数组被解释为一个二进制数（从最高有效位到最低有效位）。

返回布尔值列表 `answer`，只有当 `N_i` 可以被 `5` 整除时，答案 `answer[i]` 为 `true`，否则为 `false`。



**示例 1：**
            **输入：** [0,1,1]    **输出：** [true,false,false]    **解释：**    输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。    

**示例 2：**
            **输入：** [1,1,1]    **输出：** [false,false,false]    

**示例 3：**
            **输入：** [0,1,1,1,1,1]    **输出：** [true,false,false,false,true,false]    

**示例  4：**
            **输入：** [1,1,1,0,1]    **输出：** [false,false,false,false,false]    



**提示：**

  1. `1 <= A.length <= 30000`
  2. `A[i]` 为 `0` 或 `1`


**Tags:** Array

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # n = len(nums)
        # li, s, ans =[], '', [False]*n
        # for i in nums:
        #     s += str(i)
        #     if len(s) >1 and s[0] == '0':li.append(int(s[1:],2))
        #     else:li.append(int(s,2))
        # for i in range(n):
        #     if li[i]%5 == 0:
        #         ans[i] = True
        # return ans

        tls=[str(nums[0])]
        for i in range(1,len(nums)):
            tls.append(str(tls[i-1])+str(nums[i]))
        return [int(e,base=2)%5==0 for e in tls]
```

[title]: https://leetcode-cn.com/problems/binary-prefix-divisible-by-5
