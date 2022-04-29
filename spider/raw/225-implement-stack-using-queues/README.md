# [Implement Stack using Queues][title]

## Description

请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（`push`、`top`、`pop` 和 `empty`）。

实现 `MyStack` 类：

  * `void push(int x)` 将元素 x 压入栈顶。
  * `int pop()` 移除并返回栈顶元素。
  * `int top()` 返回栈顶元素。
  * `boolean empty()` 如果栈是空的，返回 `true` ；否则，返回 `false` 。



**注意：**

  * 你只能使用队列的基本操作 —— 也就是 `push to back`、`peek/pop from front`、`size` 和 `is empty` 这些操作。
  * 你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。



**示例：**
            **输入：**    ["MyStack", "push", "push", "top", "pop", "empty"]    [[], [1], [2], [], [], []]    **输出：**    [null, null, null, 2, 2, false]        **解释：**    MyStack myStack = new MyStack();    myStack.push(1);    myStack.push(2);    myStack.top(); // 返回 2    myStack.pop(); // 返回 2    myStack.empty(); // 返回 False    



**提示：**

  * `1 <= x <= 9`
  * 最多调用`100` 次 `push`、`pop`、`top` 和 `empty`
  * 每次调用 `pop` 和 `top` 都保证栈不为空



**进阶：** 你能否仅用一个队列来实现栈。


**Tags:** Stack, Design, Queue

**Difficulty:** Easy

## 思路

``` python3
from queue import Queue
class MyStack:

    def __init__(self):
        self.q0 = Queue()
        self.q1 = Queue()

    def push(self, x: int) -> None:
        self.q0.put(x)
        #print(self.q0.qsize())

    def pop(self) -> int:
        while self.q0.qsize()>1:
            self.q1.put(self.q0.get())
        r = self.q0.get()
        while self.q1.qsize()>0:
            self.q0.put(self.q1.get())
        return r

    def top(self) -> int:
        while self.q0.qsize()>1: self.q1.put(self.q0.get())
        t = self.q0.get()
        self.q1.put(t)
        while self.q1.qsize()>0: self.q0.put(self.q1.get())
        return t

    def empty(self) -> bool:
        return self.q0.qsize()==0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

[title]: https://leetcode-cn.com/problems/implement-stack-using-queues
