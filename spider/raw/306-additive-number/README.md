# [Additive Number][title]

## Description

**累加数** 是一个字符串，组成它的数字可以形成累加序列。

一个有效的 **累加序列** 必须 **至少** 包含 3 个数。除了最开始的两个数以外，序列中的每个后续数字必须是它之前两个数字之和。

给你一个只包含数字 `'0'-'9'` 的字符串，编写一个算法来判断给定输入是否是 **累加数** 。如果是，返回 `true` ；否则，返回
`false` 。

**说明：** 累加序列里的数，除数字 0 之外， **不会** 以 0 开头，所以不会出现 `1, 2, 03` 或者 `1, 02, 3` 的情况。



**示例 1：**
            **输入：**"112358"    **输出：** true     **解释：** 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8    

**示例  2：**
            **输入：**"199100199"    **输出：** true     **解释：** 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199



**提示：**

  * `1 <= num.length <= 35`
  * `num` 仅由数字（`0` \- `9`）组成



**进阶：** 你计划如何处理由过大的整数输入导致的溢出?


**Tags:** String, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if num =='000':return True
        num,ln=[int(e) for e in list(num)],len(num)

        def ls2n(ls):
            ln,c=len(ls),0
            for i,n in enumerate(ls):
                c+=n*10**(ln-1-i)
            return c

        def chk(num,f2,f1):
            #print(num,f2,f1)
            if not num:return True
            su= f2+f1
            d=math.ceil(math.log10(su+1))
            #print(su,d,num[:d],ls2n(num[:d]))

            if su!=ls2n(num[:d]):
                return False
            else:
                return chk(num[d:],f1,su)
        def isadn(num):
            for i in range(1,ln-1):
                if num[0]==0 and i>=2:return False
                f2 =ls2n(num[:i])
                for j in range(i+1,ln):
                    if num[i]==0 and j>=i+2: break
                    f1 = ls2n(num[i:j])
                    print('c',num[j:],f2,f1)
                    r=chk(num[j:],f2,f1)
                    if r:return True
            return False
        return isadn(num)


                    

```

[title]: https://leetcode-cn.com/problems/additive-number
