# [Print in Order][title]

## Description

给你一个类：
            public class Foo {      public void first() { print("first"); }      public void second() { print("second"); }      public void third() { print("third"); }    }

三个不同的线程 A、B、C 将会共用一个 `Foo` 实例。

  * 线程 A 将会调用 `first()` 方法
  * 线程 B 将会调用 `second()` 方法
  * 线程 C 将会调用 `third()` 方法

请设计修改程序，以确保 `second()` 方法在 `first()` 方法之后被执行，`third()` 方法在 `second()` 方法之后被执行。

**提示：**

  * 尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。
  * 你看到的输入格式主要是为了确保测试的全面性。



**示例 1：**
            **输入：** nums = [1,2,3]    **输出：** "firstsecondthird"    **解释：**    有三个线程会被异步启动。输入 [1,2,3] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 second() 方法，线程 C 将会调用 third() 方法。正确的输出是 "firstsecondthird"。    

**示例 2：**
            **输入：** nums = [1,3,2]    **输出：** "firstsecondthird"    **解释：**    输入 [1,3,2] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 third() 方法，线程 C 将会调用 second() 方法。正确的输出是 "firstsecondthird"。



**提示：**

  * `nums` 是 `[1, 2, 3]` 的一组排列


**Tags:** Concurrency

**Difficulty:** Easy

## 思路

``` python3
import queue

class Foo:
    def __init__(self):
        self.q1 = queue.Queue(1)
        self.q1.put(0)
        self.q2 = queue.Queue(1)
        self.q2.put(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.get()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.put(0)
        printSecond()
        self.q2.get()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.put(0)
        printThird()
```

[title]: https://leetcode-cn.com/problems/print-in-order
