# [Finding 3-Digit Even Numbers][title]

## Description

给你一个整数数组 `digits` ，其中每个元素是一个数字（`0 - 9`）。数组中可能存在重复元素。

你需要找出 **所有** 满足下述条件且 **互不相同** 的整数：

  * 该整数由 `digits` 中的三个元素按 **任意** 顺序 **依次连接** 组成。
  * 该整数不含 **前导零**
  * 该整数是一个 **偶数**

例如，给定的 `digits` 是 `[1, 2, 3]` ，整数 `132` 和 `312` 满足上面列出的全部条件。

将找出的所有互不相同的整数按 **递增顺序** 排列，并以数组形式返回 _。_



**示例 1：**
            **输入：** digits = [2,1,3,0]    **输出：** [102,120,130,132,210,230,302,310,312,320]    **解释：**    所有满足题目条件的整数都在输出数组中列出。     注意，答案数组中不含有 **奇数** 或带 **前导零** 的整数。

**示例 2：**
            **输入：** digits = [2,2,8,8,2]    **输出：** [222,228,282,288,822,828,882]    **解释：**    同样的数字（0 - 9）在构造整数时可以重复多次，重复次数最多与其在 digits 中出现的次数一样。     在这个例子中，数字 8 在构造 288、828 和 882 时都重复了两次。     

**示例 3：**
            **输入：** digits = [3,7,5]    **输出：** []    **解释：**    使用给定的 digits 无法构造偶数。    

**示例 4：**
            **输入：** digits = [0,2,0,0]    **输出：** [200]    **解释：**    唯一一个不含 **前导零** 且满足全部条件的整数是 200 。    

**示例 5：**
            **输入：** digits = [0,0,0]    **输出：** []    **解释：**    构造的所有整数都会有 **前导零** 。因此，不存在满足题目条件的整数。    



**提示：**

  * `3 <= digits.length <= 100`
  * `0 <= digits[i] <= 9`


**Tags:** Array, Hash Table, Enumeration, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def pem_v0(digits):
            res =set()
            for i in range(len(digits)):
                if digits[i] not in [0,2,4,6,8]:continue
                for j in range(len(digits)):
                    if i==j:continue
                    for k in range(len(digits)):
                        if k in[i,j] or digits[k]==0:continue
                        res.add(digits[k]*100+digits[j]*10+digits[i])
            return sorted(list(res))

        def perm_v1(digits):
            res = [[digits[i],[i]] for i in range(len(digits))]
            dic = {}
            for dd in range(1,3):    
                res0 = res.copy()
                for i in range(len(digits)):
                    dv =10**dd *digits[i]
                    for vv,pos in res0:
                        if len(pos)==dd and (i not in pos) and dv+vv>=(100 if dd==2 else 0) and (dv+vv not in dic) and (dv+vv)%2==0:
                            dic.setdefault(dv+vv,0)
                            res.append([dv+vv,pos+[i]])
                print(len(res))
            return sorted([el for el in list(dic.keys()) if el>=100 and el%2==0])

        return perm_v1(digits)
        
```

[title]: https://leetcode-cn.com/problems/finding-3-digit-even-numbers
