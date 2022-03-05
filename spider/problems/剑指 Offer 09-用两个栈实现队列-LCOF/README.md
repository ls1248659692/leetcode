# [用两个栈实现队列 LCOF][title]

## Description

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 `appendTail` 和 `deleteHead`
，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，`deleteHead` 操作返回 -1 )



**示例 1：**
            **输入：**    ["CQueue","appendTail","deleteHead","deleteHead"]    [[],[3],[],[]]    **输出：** [null,null,3,-1]    

**示例 2：**
            **输入：**    ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]    [[],[],[5],[2],[],[]]    **输出：** [null,-1,null,null,5,2]    

**提示：**

  * `1 <= values <= 10000`
  * `最多会对 appendTail、deleteHead 进行 10000 次调用`


**Tags:** Stack, Design, Queue

**Difficulty:** Easy

## 思路

``` python3
class CQueue:

    def __init__(self):
        self.st1 =[]
        self.st2= []


    def appendTail(self, value: int) -> None:
        self.st1.append(value)


    def deleteHead(self) -> int:
        while self.st1: self.st2.append(self.st1.pop())
        val = self.st2.pop() if self.st2 else -1
        while self.st2: self.st1.append(self.st2.pop())
        return val

```

[title]: https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
