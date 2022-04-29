# [Animal Shelter LCCI][title]

## Description

动物收容所。有家动物收容所只收容狗与猫，且严格遵守"先进先出"的原则。在收养该收容所的动物时，收养人只能收养所有动物中"最老"（由其进入收容所的时间长短而定）的动物，或者可以挑选猫或狗（同时必须收养此类动物中"最老"的）。换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，比如`enqueue`、`dequeueAny`、`dequeueDog`和`dequeueCat`。允许使用Java内置的LinkedList数据结构。

`enqueue`方法有一个`animal`参数，`animal[0]`代表动物编号，`animal[1]`代表动物种类，其中 0 代表猫，1 代表狗。

`dequeue*`方法返回一个列表`[动物编号, 动物种类]`，若没有可以收养的动物，则返回`[-1,-1]`。

**示例1:**
            **输入** ：    ["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]    [[], [[0, 0]], [[1, 0]], [], [], []]    **输出** ：    [null,null,null,[0,0],[-1,-1],[1,0]]    

**示例2:**
            **输入** ：    ["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"]    [[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]    **输出** ：    [null,null,null,null,[2,1],[0,0],[1,0]]    

**说明:**

  1. 收纳所的最大容量为20000


**Tags:** Design, Queue

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/animal-shelter-lcci
