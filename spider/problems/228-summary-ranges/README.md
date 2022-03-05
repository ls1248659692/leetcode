# [Summary Ranges][title]

## Description

给定一个   **无重复元素** 的  **有序** 整数数组 `nums` 。

返回 _**恰好覆盖数组中所有数字** 的 **最小有序** 区间范围列表 _。也就是说，`nums`
的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 `nums` 的数字 `x` 。

列表中的每个区间范围 `[a,b]` 应该按如下格式输出：

  * `"a->b"` ，如果 `a != b`
  * `"a"` ，如果 `a == b`



**示例 1：**
            **输入：** nums = [0,1,2,4,5,7]    **输出：** ["0->2","4->5","7"]    **解释：** 区间范围是：    [0,2] --> "0->2"    [4,5] --> "4->5"    [7,7] --> "7"    

**示例 2：**
            **输入：** nums = [0,2,3,4,6,8,9]    **输出：** ["0","2->4","6","8->9"]    **解释：** 区间范围是：    [0,0] --> "0"    [2,4] --> "2->4"    [6,6] --> "6"    [8,9] --> "8->9"    



**提示：**

  * `0 <= nums.length <= 20`
  * `-231 <= nums[i] <= 231 - 1`
  * `nums` 中的所有值都 **互不相同**
  * `nums` 按升序排列


**Tags:** Array

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        tn =[-99999] + nums+[-99999]
        sp=[(tn[i-1],tn[i]) for i in range(1,len(tn)) if tn[i]-tn[i-1]-1!=0]
        spb= [e for r in sp for e in r][1:-1]
        print (spb)
        spc = ['%s'%spb[i] if spb[i]==spb[i+1] else '%s->%s'%(spb[i],spb[i+1]) for i in range(0,len(spb),2)]
        print(spc)
        return spc
```

[title]: https://leetcode-cn.com/problems/summary-ranges
