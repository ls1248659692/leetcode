# [Course Schedule][title]

## Description

你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses - 1` 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 `prerequisites` 给出，其中 `prerequisites[i] = [ai, bi]`
，表示如果要学习课程 `ai` 则 **必须** 先学习课程 `bi` 。

  * 例如，先修课程对 `[0, 1]` 表示：想要学习课程 `0` ，你需要先完成课程 `1` 。

请你判断是否可能完成所有课程的学习？如果可以，返回 `true` ；否则，返回 `false` 。

**示例 1：**
            **输入：** numCourses = 2, prerequisites = [[1,0]]    **输出：** true    **解释：** 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

**示例 2：**
            **输入：** numCourses = 2, prerequisites = [[1,0],[0,1]]    **输出：** false    **解释：** 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

**提示：**

  * `1 <= numCourses <= 105`
  * `0 <= prerequisites.length <= 5000`
  * `prerequisites[i].length == 2`
  * `0 <= ai, bi < numCourses`
  * `prerequisites[i]` 中的所有课程对 **互不相同**


**Tags:** Depth-First Search, Breadth-First Search, Graph, Topological Sort

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def canFinish(self, num: int, req: List[List[int]]) -> bool:
        d={}
        for b,a in req:
            d.setdefault(b,set()).add(a)
            #d[b].add(a)
        print(d)
        for b in d:
            aset,tset=set(d[b]),set(d[b])
            print('tset_begin',b,tset)
            while aset:
                _aset,aset=set(aset),set()
                for bb in _aset:
                    for a in d.get(bb,set()):
                        if a not in tset:aset.add(a)
                for e in aset:tset.add(e)
            print('tset_end',b,tset)
            if b in tset:return False
        return True
```

[title]: https://leetcode-cn.com/problems/course-schedule
