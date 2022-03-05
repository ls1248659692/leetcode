# [Reordered Power of 2][title]

## Description

给定正整数 `n` ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。

如果我们可以通过上述方式得到 2 的幂，返回 `true`；否则，返回 `false`。



**示例 1：**
            **输入：** n = 1    **输出：** true    

**示例 2：**
            **输入：** n = 10    **输出：** false    



**提示：**

  * `1 <= n <= 109`


**Tags:** Math, Counting, Enumeration, Sorting

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def check_v3(n):
            numstr2digcount=lambda num_str: {num_dig:num_str.count(str(num_dig)) for num_dig in range(10) }
            chklst = [str(2 ** ii) for ii in range(30)]
            print(chklst)
            return True if numstr2digcount(str(n)) in [numstr2digcount(e) for e in chklst] else False

        def check_v1(n):
            def perm_v1(digits):
                res = [[digits[i],[i]] for i in range(len(digits)) if digits[i]%2==0]
                dic = {}
                dic_s={}
                for dd in range(1,len(digits)):    
                    res0 = res.copy()
                    #print(dic_s)
                    for i in range(len(digits)):
                        if i==len(digits) and digits[i]==0:continue
                        dv =10**dd *digits[i]
                        for vv,pos in res0:
                            dv_str = '0'*(dd+1-len(str(dv+vv)))+str(dv+vv)
                            if len(pos)==dd and (i not in pos) and dv_str not in dic_s:
                                dic_s.setdefault(dv_str,0)
                                dic.setdefault(dv+vv,0)
                                res.append([dv+vv,pos+[i]])
                    #print(len(res))
                #print(dic)
                return sorted([el for el in list(dic.keys()) if len(str(el))==len(digits) and log2(el)==int(log2(el))])

            sli = [int(e) for e in str(n)]
            if n<100:return  n in [0,1,2,4,8,16,61,32,23,64,46]
            rset = perm_v1(sli)
            return  True if rset else False

        return check_v3(n)
```

[title]: https://leetcode-cn.com/problems/reordered-power-of-2
