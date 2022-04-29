# [最近最少使用缓存][title]

## Description

运用所掌握的数据结构，设计和实现一个  [LRU (Least Recently Used，最近最少使用)
缓存机制](https://baike.baidu.com/item/LRU) 。

实现 `LRUCache` 类：

  * `LRUCache(int capacity)` 以正整数作为容量 `capacity` 初始化 LRU 缓存
  * `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1` 。
  * `void put(int key, int value)` 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。



**示例：**
            **输入**    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]    **输出**    [null, null, null, 1, null, -1, null, -1, 3, 4]        **解释**    LRUCache lRUCache = new LRUCache(2);    lRUCache.put(1, 1); // 缓存是 {1=1}    lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}    lRUCache.get(1);    // 返回 1    lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}    lRUCache.get(2);    // 返回 -1 (未找到)    lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}    lRUCache.get(1);    // 返回 -1 (未找到)    lRUCache.get(3);    // 返回 3    lRUCache.get(4);    // 返回 4    



**提示：**

  * `1 <= capacity <= 3000`
  * `0 <= key <= 10000`
  * `0 <= value <= 105`
  * 最多调用 `2 * 105` 次 `get` 和 `put`



**进阶** ：是否可以在 `O(1)` 时间复杂度内完成这两种操作？



注意：本题与主站 146 题相同：<https://leetcode-cn.com/problems/lru-cache/>


**Tags:** Design, Hash Table, Linked List, Doubly-Linked List

**Difficulty:** Medium

## 思路

``` python3
class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

[title]: https://leetcode-cn.com/problems/OrIXps
