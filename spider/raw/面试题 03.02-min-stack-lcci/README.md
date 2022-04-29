# [Min Stack LCCI][title]

## Description

请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。

  

 **示例：**
            MinStack minStack = new MinStack();      minStack.push(-2);      minStack.push(0);      minStack.push(-3);      minStack.getMin();   --> 返回 -3.      minStack.pop();      minStack.top();      --> 返回 0.      minStack.getMin();   --> 返回 -2.


**Tags:** Stack, Design

**Difficulty:** Easy

## 思路

``` python3
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.li=[]

    def push(self, x: int) -> None:
        self.li.append(x)


    def pop(self) -> None:
        self.li.pop()


    def top(self) -> int:
        return self.li[-1]


    def getMin(self) -> int:
        return min(self.li)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

[title]: https://leetcode-cn.com/problems/min-stack-lcci
