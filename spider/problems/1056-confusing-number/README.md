# [Confusing Number][title]

## Description

给定一个数字 `N`，当它满足以下条件的时候返回 `true`：

原数字旋转 180° 以后可以得到新的数字。

如 0, 1, 6, 8, 9 旋转 180° 以后，得到了新的数字 0, 1, 9, 8, 6 。

2, 3, 4, 5, 7 旋转 180° 后，得到的 **不是** 数字。

易混淆数 (confusing number) 在旋转180°以后，可以得到和原来 **不同** 的数，且新数字的每一位都是有效的。



**示例 1：**

![](https://assets.leetcode.com/uploads/2019/03/23/1268_1.png)
            **输入：** 6    **输出：** true    **解释：** 把 6 旋转 180° 以后得到 9，9 是有效数字且 9!=6 。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2019/03/23/1268_2.png)
            **输入：** 89    **输出：** true    **解释:** 把 89 旋转 180° 以后得到 68，86 是有效数字且 86!=89 。    

**示例 3：**

![](https://assets.leetcode.com/uploads/2019/03/26/1268_3.png)
            **输入：** 11    **输出：** false    **解释：** 把 11 旋转 180° 以后得到 11，11 是有效数字但是值保持不变，所以 11 不是易混淆数字。     

**示例 4：**

![](https://assets.leetcode.com/uploads/2019/03/23/1268_4.png)
            **输入：** 25    **输出：** false    **解释：**    把 25 旋转 180° 以后得到的不是数字。    



**提示：**

  1. `0 <= N <= 10^9`
  2. 可以忽略掉旋转后得到的前导零，例如，如果我们旋转后得到 `0008` 那么该数字就是 `8` 。


**Tags:** Math

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def confusingNumber(self, n: int) -> bool:
        dic = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        s = str(n)
        res = ""
        for c in s:
            if c not in dic:
                return False
            res = dic[c] + res
        return res != s

```

[title]: https://leetcode-cn.com/problems/confusing-number
