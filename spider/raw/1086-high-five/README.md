# [High Five][title]

## Description

给你一个不同学生的分数列表 `items`，其中 `items[i] = [IDi, scorei]` 表示 `IDi`
的学生的一科分数，你需要计算每个学生 **最高的五科** 成绩的 **平均分** 。

返回答案 `result` 以数对数组形式给出 _，_ 其中 __`result[j] = [IDj, topFiveAveragej]` __ 表示
__`IDj` __ 的学生和他 **最高的五科** 成绩的 **平均分** _。_`result` __ 需要按 __`IDj` __ 递增的
**顺序排列** 。

学生 **最高的五科** 成绩的 **平均分** 的计算方法是将最高的五科分数相加，然后用 **整数除法** 除以 5 。

**示例 1：**
            **输入：** items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]    **输出：** [[1,87],[2,88]]    **解释：**    ID = 1 的学生分数为 91、92、60、65、87 和 100 。前五科的平均分 (100 + 92 + 91 + 87 + 65) / 5 = 87    ID = 2 的学生分数为 93、97、77、100 和 76 。前五科的平均分 (100 + 97 + 93 + 77 + 76) / 5 = 88.6，但是由于使用整数除法，结果转换为 88    

**示例 2：**
            **输入：** items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]    **输出：** [[1,100],[7,100]]    

**提示：**

  * `1 <= items.length <= 1000`
  * `items[i].length == 2`
  * `1 <= IDi <= 1000`
  * `0 <= scorei <= 100`
  * 对于每个 `IDi`， **至少** 存在五个分数


**Tags:** Array, Hash Table, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        for x, y in items:
            dic[x].append(y)
        ans = []
        for key, val in dic.items():
            tmp = sum(sorted(val)[::-1][:5]) // 5
            ans.append([key, tmp])
        ans.sort(key=lambda x: x[0])
        return ans

```

[title]: https://leetcode-cn.com/problems/high-five
