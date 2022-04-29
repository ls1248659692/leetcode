# [X of a Kind in a Deck of Cards][title]

## Description

给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 `X`，使我们可以将整副牌按下述规则分成 1 组或更多组：

  * 每组都有 `X` 张牌。
  * 组内所有的牌上都写着相同的整数。

仅当你可选的 `X >= 2` 时返回 `true`。



**示例 1：**
            **输入：** deck = [1,2,3,4,4,3,2,1]    **输出：** true    **解释：** 可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]    

**示例 2：**
            **输入：** deck = [1,1,1,2,2,2,3,3]    **输出：** false    **解释：** 没有满足要求的分组。    

  
**提示：**

  * `1 <= deck.length <= 104`
  * `0 <= deck[i] < 104`


**Tags:** Array, Hash Table, Math, Counting, Number Theory

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)==1: return False
        ct=[deck.count(n) for n in set(deck)]
        print(ct)
        sc = set(ct)
        mi = min(ct)
        if ct==1:return False
        for mmi in range(2,mi+1):
            if sum(c%mmi for c in ct)==0:return True
        return False
```

[title]: https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards
