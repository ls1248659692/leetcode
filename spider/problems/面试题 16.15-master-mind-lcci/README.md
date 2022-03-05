# [Master Mind LCCI][title]

## Description

珠玑妙算游戏（the game of master mind）的玩法如下。

计算机有4个槽，每个槽放一个球，颜色可能是红色（R）、黄色（Y）、绿色（G）或蓝色（B）。例如，计算机可能有RGGB
4种（槽1为红色，槽2、3为绿色，槽4为蓝色）。作为用户，你试图猜出颜色组合。打个比方，你可能会猜YRGB。要是猜对某个槽的颜色，则算一次“猜中”；要是只猜对颜色但槽位猜错了，则算一次“伪猜中”。注意，“猜中”不能算入“伪猜中”。

给定一种颜色组合`solution`和一个猜测`guess`，编写一个方法，返回猜中和伪猜中的次数`answer`，其中`answer[0]`为猜中的次数，`answer[1]`为伪猜中的次数。

**示例：**
            **输入：** solution="RGBY",guess="GGRR"    **输出：** [1,1]    **解释：** 猜中1次，伪猜中1次。    

**提示：**

  * `len(solution) = len(guess) = 4`
  * `solution`和`guess`仅包含`"R"`,`"G"`,`"B"`,`"Y"`这4种字符


**Tags:** Hash Table, String, Counting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        s,g=solution,guess
        hits = [i for i in range(4)if s[i]==g[i]]
        exh_s = [s[i] for i in range(4)if s[i]!=g[i]]
        
        phits = [g[i] for i in range(4) if s[i]!=g[i] and g[i] in exh_s and i not in hits ]
        phits_1 = [min(phits.count(co),s.count(co)) for co in set(phits)]
        print(hits,phits,phits_1)
        return[len(hits),sum([e for e in phits_1])]
```

[title]: https://leetcode-cn.com/problems/master-mind-lcci
