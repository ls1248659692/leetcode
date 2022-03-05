# [包含min函数的栈 LCOF][title]

## Description

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。



**示例:**
            MinStack minStack = new MinStack();    minStack.push(-2);    minStack.push(0);    minStack.push(-3);    minStack.min();   --> 返回 -3.    minStack.pop();    minStack.top();      --> 返回 0.    minStack.min();   --> 返回 -2.    



**提示：**

  1. 各函数的调用总次数不超过 20000 次



注意：本题与主站 155 题相同：<https://leetcode-cn.com/problems/min-stack/>


**Tags:** Stack, Design

**Difficulty:** Easy

## 思路

``` python3
class MinStack:

    def __init__(self):
        self.li=[]

    def push(self, val: int) -> None:
        self.li.append(val)


    def pop(self) -> None:
        self.li.pop()

    def top(self) -> int:
        return self.li[-1]


    def min(self) -> int:
        return min(self.li) if self.li else None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
```

[title]: https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
