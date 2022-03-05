## Leetcode -- 一步一步成为 offer 收割机 (算法全都是套路，牢记算法模板，offer拿到手软)

> 作者： Jam
> + 个人简介： 化工行业转行计算机全靠自学，目前在国内大厂工作，在力扣上传了数百道问题的解法，本仓库主要是为了总结算法套路与帮助和我一样转行，以及想深入学习算法有大厂梦的兄弟和姐妹们。

**算法题分类思维导图：**
![image](https://user-images.githubusercontent.com/33345911/155837010-d97e1df7-0261-4099-8039-6b31cf567b70.png)

本仓库的 leetcode 文件夹下都是基于 LeetCode 的题目，涵盖了所有题型和技巧，而且一定要做到**举一反三，通俗易懂**，[算法体系化学习书籍和面试题](https://github.com/ls1248659692/leetcode/tree/master/book)有相关算法系统学习书籍和题目推荐。

## Leetcode [算法题刷题科学刷题总结](https://zhuanlan.zhihu.com/p/96883783)
1. 职业训练：拆分知识点、刻意练习、总结
2. 五步刷题法（五毒神掌）
3. 做算法的最大误区：只刷一遍
4. 新手建议先从简单题开始刷起，从30min/题 提升到 5min/题 就可以开始挑战刷中等难度题
5. 大厂面试只要你能不看答案刷中等难度题，基本国内大厂随便进



### 面试技巧：
1. 确定和面试官沟通的是否一致，问清楚，题目要看清楚
2. 想所有可能的解法，找时间最优解法
3. coding（多写）
4. test cases（测试样例）

### 五毒神掌内功心法
#### 第一遍：
1. 读题：5分钟读题+思考
2. 直接看解法（理解多个解法）
3. 背诵默写
#### 第二遍：
1. 马上自己写，提交lc（leetcode）
2. 多种解法比较，体会->优化（执行时间和ac）
#### 第三遍：（24小时之后）
1. 过了一天再重复做题
2. 不同熟悉的解法程度->专项训练
#### 第四遍：（1周后）
1. 过了一周：再反复练习相同题目
2. 专项训练
#### 第五遍：（面试前一周）
1. 面试前一周恢复训练
2. 面试前一周复习算法模板与相应分类出现的题目


## 算法题汇总

20 个最常用的、最基础数据结构与算法，都已经总结在 [算法题模板分类](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates)

10 个必考数据结构模板：数组、链表、栈、队列、散列表、二叉树、堆、跳表、图、Trie 树。

10 个必会算法模板：递归、排序、二分查找、搜索、哈希算法、贪心算法、分治算法、回溯算法、动态规划、字符串匹配算法。

### 不同算法类型
>1. [滑动窗口](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/sliding_window)
>2. [双指针](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/two_pointers)
>3. [快慢指针链表](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/linked_list)
>4. [集合查找](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/union_find)
>5. [二叉树](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/trie_tree)
>6. [字符串](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/string)
>7. [DFS](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/dfs)
>8. [BFS](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/bfs)
>9. [回溯法](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/backtracking)
>10. [双堆模式](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/heap)
>11. [二分法与二分法变种](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/binary_search)
>12. [前K大的数模式HEAP](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/heap)
>13. [分治思想](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/divide_conquer)
>14. [DP 动态规划](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/dynamic_programming)
>15. [排序算法](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/sort)
>16. [链表](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/linked_list)
>17. [二叉搜索树的构建](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/binary_tree)
>18. [位运算](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/bit_manipulation)
>19. [dict](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/dict)
>20. [stack](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/stack)/[queue](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/queue)
>21. [math](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/match)
>22. [array](https://github.com/ls1248659692/leetcode/blob/master/algorithm_templates/array/array_examples.py)
>23. [图](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/graph)
>24. [贪婪算法](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/greedy)
>25. [matrix](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/matrix)
>26. [一般算法题模板](https://github.com/ls1248659692/leetcode/tree/master/algorithm_templates/common)

## 题型汇总

### `1. 滑动窗口`
>53. 大小为 K 的子数组的最大和
>121. Best Time to Buy and Sell Stock
>3. Longest Substring Without Repeating Characters
>239. Sliding Window Maximum
>* 剑指 Offer 57 - II. 和为s的连续正数序列
```python3
# Sliding windows code template is most used in substring match or maximum/minimum problems.
# It uses two-pointer as boundary of sliding window to traverse, and use a counter(dict) maintain current state,
# and a count as condition checker, update it when trigger some key changes.
#
# Time:  O(n)
# Space: O(k) k = len(set(p))
from collections import Counter

# s - target sequence, p - pattern or restrict sequence
def sliding_window_template_with_examples(s, p):
    # initialize the hash map here
    # counter is used to record current state, could use defaultdict in some situation, for example, no p restrict
    counter = Counter(p)

    # two pointers, boundary of sliding window
    start, end = 0, 0
    # condition checker, update it when trigger some key changes, init value depend on your situation
    count = 0
    # result, return int(such as max or min) or list(such as all index)
    res = 0

    # loop the source string from begin to end
    while end < len(s):
        counter[s[end]] += 1
        # update count based on some condition
        if counter[s[end]] > 1:
            count += 1
        end += 1

        # count condition here
        while count > 0:
            '''
            update res here if finding minimum
            '''

            # increase start to make it invalid or valid again
            counter[s[start]] -= 1
            # update count based on some condition
            if counter[s[start]] > 0:
                count -= 1
            start += 1

        '''
        update res here if finding maximum
        '''
        res = max(res, end - start)

    return res

# refer to https://leetcode.com/problems/minimum-window-substring/discuss/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems
```

### `2. 双指针`
>双指针通常用在排好序的数组或是链表中寻找对子, 或者是merge 或者是排序，或者去除element，反正一般都是头尾各一个指针，然后根据条件移动。

>1. Two Sum（# 也可以用map的方式做）
>167. Two Sum II - Input array is sorted
>977. Squares of a Sorted Array (很像merge sort里的merge）
>283. Move Zeroes
>27. Remove Element
>26. Remove Duplicates from Sorted Array
>16. 3Sum Closest
>18. 4Sum
>86. Partition List
>11. Container With Most Water
>42. Trapping Rain Water
>75. Sort Colors
>* 剑指 Offer 04. 二维数组中的查找
>* 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
```python3
# two pointers scenario, famous applications such as binary search, quick sort and sliding window.

'''
Classification:
1. old & new state: old, new = new, cur_result
2. slow & fast runner: slow-> fast->->
3. left & right boundary or index: left-> <-right
4. p1 & p2 from two sequences: p1-> p2->
5. start & end sliding window boundary: start-> end->
'''


# old & new state: old, new = new, cur_result
def old_new_state(self, seq):
    # initialize state
    old, new = default_val1, default_val2
    for element in seq:
        '''
        process current element with old state
        '''
        old, new = new, self.process_logic(element, old)


# slow & fast runner: slow-> fast->->
def slow_fast_runner(self, seq):
    # initialize slow runner
    slow = seq[0]   # for index: slow = 0
    # fast-runner grows each iteration generally
    for fast in range(seq):     # for index: range(len(seq))
        '''
        slow-runner grows with some restrictions
        '''
        if self.slow_condition(slow):
            slow = slow.next    # for index: slow += 1
        '''
        process logic before or after pointers movement
        '''
        self.process_logic(slow, fast)


# left & right boundary or index: left-> <-right
def left_right_boundary(self, seq):
    left, right = 0, len(seq) - 1
    while left < right:
        '''
        left index moves when satisfy the condition
        '''
        if self.left_condition(left):
            left += 1

        '''
        right index move when satisfy the condition
        '''
        if self.right_condition(right):
            right -= 1

        '''
        process logic before or after pointers movement
        '''
        self.process_logic(left, right)


# p1 & p2 from two sequences: p1-> p2->
def pointers_from_two_seq(self, seq1, seq2):
    # init pointers
    p1, p2 = 0, 0       # or seq1[0], seq2[0]

    # or other condition
    while p1 < len(seq1) and p2 < len(seq2):
        '''
        p1 index moves when satisfy the condition
        '''
        if self.p1_condition(p1):
            p1 += 1         # or p1 = next(seq1)

        '''
        p2 index move when satisfy the condition
        '''
        if self.p2_condition(p2):
            p2 += 1         # or p2 = next(seq2)

        '''
        process logic before or after pointers movement
        '''
        self.process_logic(p1, p2)


# start & end of sliding window: |start-> ... end->|
# more details in sliding windows templates, here is just about two-pointers part
def start_end_sliding_window(self, seq):
    start, end = 0, 0

    while end < len(seq):
        # end grows in the outer loop
        end += 1

        # start grows with some restrict
        while self.start_condition(start):
            '''
            process logic before pointers movement
            '''
            self.process_logic1(start, end)

            # start grows in the inner loop
            start += 1

        '''
        or process logic after pointers movement
        '''
        self.process_logic2(start, end)
```

### `3. 快慢指针/ 链表题目`
>快慢指针是处理linked list常用的套路，通常是用来判断成环以及环的入口，或者是寻找 list中第k个元素。

>141. Linked List Cycle
>142. Linked List Cycle II
>234. Palindrome Linked List
>61. Rotate List
>* 剑指 Offer 18. 删除链表的节点
>JZ56 删除链表中重复的结点
>* 剑指 Offer 22. 链表中倒数第k个节点
>* 剑指 Offer 52. 两个链表的第一个公共节点
```python3
# a Linked list is a linear collection of data elements, whose order is not given by their physical placement in memory.
# Instead, each element points to the next.
#
# when operation with linked list, we can choose to change list node or change node value.
# change node value is more easy-understanding, and may need extra space to store.
#
# Time:  O(1) to insert and delete, O(n) to random access
# Space: O(n)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# add dummy node to help flag the head, usually used in head may changed or merging None edge case.
def dummy_node_assist(self, head):
    dummy = ListNode(0)
    cur = dummy.next = head  # or cur = dummy

    while cur:
        '''
        process current node logic 
        '''
        self.process_logic(cur)

    return dummy.next


# another solution is use self.next, more pythonic
def self_assist(self, head):
    pre, pre.next = self, head

    while pre.next:
        '''
        process current node logic 
        '''
        self.process_logic(pre.next)

    return self.next


# add node
def add_node(pre_node, new_node):
    pre_node.next, new_node = new_node, pre_node.next


# delete node
def delete_node(pre_node):
    pre_node.next = pre_node.next.next


# reverse linked list iteratively
def reverse_iteratively(head: ListNode) -> ListNode:
    prev, cur = None, head
    while cur:
        cur.next, cur, prev = prev, cur.next, cur
    return prev


# reverse linked list recursively
def reverse_recursively(head: ListNode) -> ListNode:
    def recursive(cur, pre=None):
        if not cur:
            return pre
        pre, cur.next = cur.next, pre
        return recursive(pre, cur)

    return recursive(head)

```

### `4. 原地链表翻转`
>234. Palindrome Linked List
>206. Reverse Linked List
>25. Reverse Nodes in k-Group
>92. Reverse Linked List II

```python3
# a Linked list is a linear collection of data elements, whose order is not given by their physical placement in memory.
# Instead, each element points to the next.
#
# when operation with linked list, we can choose to change list node or change node value.
# change node value is more easy-understanding, and may need extra space to store.
#
# Time:  O(1) to insert and delete, O(n) to random access
# Space: O(n)


# reverse linked list iteratively
def reverse_iteratively(head: ListNode) -> ListNode:
    prev, cur = None, head
    while cur:
        cur.next, cur, prev = prev, cur.next, cur
    return prev


# reverse linked list recursively
def reverse_recursively(head: ListNode) -> ListNode:
    def recursive(cur, pre=None):
        if not cur:
            return pre
        pre, cur.next = cur.next, pre
        return recursive(pre, cur)

    return recursive(head)
```

### `5. 区间合并`
>区间合并的问题，通常是重新把区间按照start和end排序，重新组合区间。

>56. Merge Intervals
>986. Interval List Intersections
>57. Insert Interval

```python3
todo Merge Intervals algorithm template 
```

### `6. 无序限定范围的数组元素查找O(N）`
>要求 inplace， 通常是采用正负反转的做法

>41. First Missing Positive
>448. Find All Numbers Disappeared in an Array
>剑指 Offer 03. 数组中重复的数字

```python3
todo 无序限定范围的数组元素查找O(N） algorithm template 
```

### `7. BFS`
>BFS 通常采用queue 来实现

>102. Binary Tree Level Order Traversal
>103. Binary Tree Zigzag Level Order Traversal
>297. Serialize and Deserialize Binary Tree
>127. Word Ladder I
>207. Course Schedule【拓扑排序】

```python3
# Breadth-first search is traversing or searching tree or graph data structures, including graph-like solution space.
# it explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
#
# Time:  O(V+E)     V: vertex, E: edges
# Space: O(V)
from collections import deque


# iteration version, using deque
def bfs_iteratively_by_queue(self, start, target=None):
    queue, visited = deque([start]), {start}

    while queue:
        node = queue.popleft()
        visited.add(node)
        '''
        process current node logic here
        '''
        self.process_logic(node)

        # target is optional
        if node == target:
            '''
            reach the goal and break out
            '''
            self.process_target_logic(target)
            break
        for next_node in node.get_successors():
            if next_node not in visited:
                queue.append(next_node)


# iteration version, using list, pythonic-style
# conciser but more memory, mainly used when you want to collect the whole list
def bfs_iteratively_by_list(self, start, target=None):
    node_list, visited = [start], {start}

    # append while traversing
    for node in node_list:
        visited.add(node)
        '''
        process current node logic here
        '''
        self.process_logic(node)

        # target is optional
        if node == target:
            '''
            reach the goal and break out
            '''
            self.process_target_logic(target)
            break
        for next_node in node.get_successors():
            if next_node not in visited:
                node_list += node

    # basically the node_list is useful here
    return node_list


# recursion version, uncommon
def bfs_recursively(self, queue: deque, visited: set, target=None):
    if not queue:
        return

    node = queue.popleft()
    visited.add(node)
    '''
    process current node logic here
    '''
    self.process_logic(node)

    # target is optional
    if node == target:
        '''
        reach the goal and break out
        '''
        self.process_target_logic(target)
        return
    for next_node in node.get_successors():
        if next_node not in visited:
            queue.append(next_node)
    self.bfs_recursively(queue, visited)


# bfs list comprehension in row of binary tree
def bfs_row(self, root):
    row = [root]
    while row:
        '''
        process current node logic here
        '''
        # process logic separately
        row = [child for node in row for child in (node.left, node.right) if node]

```

### `8. 树的DFS`
>通常采用递归 111. Minimum Depth of Binary Tree

>112. Path Sum
>113. Path Sum II（和剑指 Offer 34. 二叉树中和为某一值的路径一样）
>437. Path Sum III
>100. Same Tree
>101. Symmetric Tree
>104. Maximum Depth of Binary Tree
>110. Balanced Binary Tree
>* 剑指 Offer 26. 树的子结构
>* 剑指 Offer 33. 二叉搜索树的后序遍历序列
>* 剑指 Offer 54. 二叉搜索树的第k大节点(inorder)

```python3

# Deep-first search is traversing or searching tree or graph data structures, including graph-like solution space.
# it starts at the root node and explores as far as possible along each branch before backtracking.
#
# Time:  O(V+E)     V: vertex, E: edges
# Space: O(V)


# recursion version
def dfs_recursively(self, node, visited: set):
    visited.add(node)
    '''
    process current node logic here
    '''
    self.process_logic(node)

    for next_node in node.get_successors():
        if next_node not in visited:
            self.dfs_recursively(next_node, visited)


# iteration version, uncommon
def dfs_iteratively(self, root):
    stack, visited = [root], set()
    while stack:
        node = stack.pop()
        visited.add(node)
        '''
        process current node logic here
        '''
        self.process_logic(node)

        for next_node in node.get_successors():
            if next_node not in visited:
                stack.append(next_node)

```



### `9. DFS/递归/回溯法`
>对于排列和组合的题目，需要主要判断是否会有重复数字，如有重复，需要先进行sort，而且需要进行剪枝。

>78. Subsets
>90. Subsets II
>46. Permutations
>47. Permutations II
>39. Combination Sum
>322. Coin Change
>518. Coin Change 2
>40. Combination Sum II
>131. Palindrome Partitioning !
>17. Letter Combinations of a Phone Number (differ from 91. Decode Ways)
>79. Word Search(same as 剑指 Offer 12. 矩阵中的路径)
>* 剑指 Offer 13. 机器人的运动范围
>10. 双堆模式
>295 Find-Median-from-Data-Stream
>480. Sliding Window Median
>155. Min Stack
>* 剑指 Offer 09. 用两个栈实现队列

```python3
# Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably
#  constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate
#  ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
#
# backtracking vs. dfs
# traverse in solution space vs. traverse in data structure space, pruned of dfs

def backtracking(self, data, candidate):
    # pruning
    if self.reject(data, candidate):
        return

    # reach the end
    if self.accept(data, candidate):
        return self.output(data, candidate)

    # drill down
    for cur_candidate in self.all_extension(data, candidate):
        # or you can choose to prune here, recursion depth - 1
        if not self.should_to_be_pruned(cur_candidate):
            self.backtracking(data, cur_candidate)
```

### `11. 二分法与二分法变种`
>当你需要解决的问题的输入是排好序的数组，链表，或是排好序的矩阵，要求咱们寻找某些特定元素。这个时候的不二选择就是二分搜索。

>35. Search Insert Position
>34. Find First and Last Position of Element in Sorted Array
>33. Search in Rotated Sorted Array
>153. Find Minimum in Rotated Sorted Array
>154. Find Minimum in Rotated Sorted Array II(same as [剑指 Offer 11. 旋转数组的最小数字])
>162. Find Peak Element
>540. Single Element in a Sorted Array
>* 剑指 Offer 16. 数值的整数次方(2分法)

```python3
# binary search requires sorted iterator. Common variation is find left-most or right-most index.
#
# Time:  O(log(n))
# Space: O(1)


# [lo, hi] version
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        # no overflow problem in python, (lo + hi) // 2 is better.
        # mid = lo + (hi - lo) // 2
        mid = (lo + hi) // 2
        '''
        change to your comparison condition as you need
        '''
        # find the target
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1


# [lo, hi) version
def binary_search2(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        # find the target
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid


# result in [0, hi]
def bisect_left(arr, target, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        # left-most, so equal will be on the right side
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
        '''
        # bisect right code
        if arr[mid] > target:
            hi = mid
        else:
            lo = mid + 1
        '''
    return lo

```

### `12. 前K大的数模式HEAP`
>采用priority queue 或者 说在python 中的heapq 求top k 采用最小堆（默认） 采用最大堆的时候可以采用push 负的value

>215. Kth Largest Element in an Array
>347. Top K Frequent Elements
>373. Find K Pairs with Smallest Sums

```python3
# heap, also called priority queue
# heap common operations: heapify, top, heappush, heappop, heappushpop, heapreplace, _siftup/_siftdown,
# nlargest/nsmallest, merge
# heapq in Python, there is only min heap, if you want to a max heap, you should reverse the key or implement __lt__.
#
# Time:  O(1) to find, O(log(n)) to push/pop/sift, O(nlog(n)) to heapify, O(n) to merge
# Space: O(n)
#
# from Queue import PriorityQueue is alternative way, which is a thread-safe class
import heapq


def heap_operations():
    heap = [4, 2, 1, 3]

    # heapify
    heapq.heapify(heap)

    # top
    top = heap[0]

    # heappop
    top = heapq.heappop(heap)

    # heappush
    heapq.heappush(heap, 5)

    # heappushpop = push + pop
    heapq.heappushpop(heap, 0)

    # heapreplace = pop + push
    heapq.heapreplace(heap, 0)

    data = [10, 5, 18, 2, 37, 3, 8, 7, 19, 1]
    heapq.heapify(data)
    old, new = 8, 22  # increase the 8 to 22
    i = data.index(old)
    data[i] = new
    # _siftup, from root to leaf, when increase
    heapq._siftup(data, i)

    old, new = 10, 4  # decrease the 10 to 4
    i = data.index(old)
    data[i] = new
    # _siftdown, from leaf to root, when decrease
    heapq._siftdown(data, 0, i)

    # find n largest by queue
    heapq.nlargest(data, 3)

    # find n smallest by queue
    heapq.nsmallest(data, 3)

    # Merge multiple sorted inputs into a single sorted output
    # e.g. merge timestamped entries from multiple log files
    heapq.merge([1, 3, 5, 7], [0, 2, 4, 8], [5, 10, 15, 20], [], [25])

```

### `13. K路归并`
>K路归并能帮咱们解决那些涉及到多组排好序的数组的问题。

>23. Merge k Sorted Lists
>21. Merge Two Sorted Lists

```python3
todo K路归并 algorithm template
```

### `14. DP 动态规划`
>300. Longest Increasing Subsequence
>1143. Longest Common Subsequence
>72. Edit Distance
>44. Wildcard Matching
>10. Regular Expression Matching
>120. Triangle
>53. Maximum Subarray
>152. Maximum Product Subarray
>887. Super Egg Dropref
>198. House Robber
>213. House Robber II (两个dp）
>121. Best Time to Buy and Sell Stock
>122. Best Time to Buy and Sell Stock II
>188. Best Time to Buy and Sell Stock IV
>123. Best Time to Buy and Sell Stock III ref
>714. Best Time to Buy and Sell Stock with Transaction Fee
>309. Best Time to Buy and Sell Stock with Cooldown
>516. Longest Palindromic Subsequence !
>5. Longest Palindromic Substring
>416. Partition Equal Subset Sum
>322. Coin Change
>518. Coin Change 2
>91. Decode Ways
>139. Word Break
>* 剑指 Offer 10- I. 斐波那契数列
>* 剑指 Offer 10- II. 青蛙跳台阶问题
>矩形覆盖
>变态跳台阶
>* 剑指 Offer 14- I. 剪绳子
>* 剑指 Offer 46. 把数字翻译成字符串
>* 剑指 Offer 47. 礼物的最大价值
>* 剑指 Offer 49. 丑数
>* 剑指 Offer 60. n个骰子的点数

```python3
# simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner
# dynamic programming = recursion + memorized
# state definition, state transition equation, optimal substructure
# direction: bottom-up or top-down


def dynamic_programming_template_with_example(word1, word2):
    m, n = len(word1), len(word2)

    # states definition: cur_min_edit_dist
    # states compressed to two states: old and new
    dp = [[0] * (m + 1) for _ in range(2)]

    # initialize the initial edit distance, add one more state for init state
    for i in range(0, m + 1):
        dp[0][i] = i

    cur = 1
    for i in range(n):
        # initialize the init state
        dp[cur][0] = i + 1
        for j in range(m):
            # state transition equation
            # if char matched, this is the min dist.
            if word1[j] == word2[i]:
                dp[cur][j + 1] = dp[cur ^ 1][j]
            # otherwise, 1 + minimum of edit/remove/add operations
            else:
                dp[cur][j + 1] = 1 + min(dp[cur ^ 1][j], dp[cur ^ 1][j + 1], dp[cur][j])
        # switch between two states
        cur ^= 1
    # return the last state as result
    return dp[cur ^ 1][-1]
    
```

### `15. 排序算法`

>* Selection Sort
>* Heapsort
>* Mergesort
>* Insertion Sort
>* Shell's Sort
>* Quicksort
>* Bubblesort
>* Linear Sorting

```python3
# all kinds of sort algorithm, just some common versions to show its idea.
# here I unify the api as xxx_sort(arr), changed in-place
#
# currently include:
# quick, merge, insert, bubble, selection, heap, shell, bucket, counting, radix, topological
#
# constant space vs extra space (merge O(n), counting O(k), bucket O(n+k), radix O(n+k))
#
# in place vs out place (merge, counting, bucket, radix)
#
# stable vs unstable (selection, quick, heap, shell)
#
# comparison based vs non-comparison based (radix, bucket, counting)
#
# comparison of counting, bucket and radix sort: all use bucket idea
# counting sort:  store the single key in bucket
# bucket sort:    store a range in bucket
# radix sort:     store each part of element in bucket

# sort      average     best        worst       space   place       stable      comparison
# bubble    O(n^2)      O(n)        O(n^2)      O(1)    in-place    stable      comparison
# selection O(n^2)      O(n^2)      O(n^2)      O(1)    in-place    unstable    comparison
# insert    O(n^2)      O(n)        O(n^2)      O(1)    in-place    stable      comparison
# shell     O(nlogn)    O(nlogn^2)  O(nlogn^2)  O(1)    in-place    unstable    comparison
# merge     O(nlogn)    O(nlogn)    O(nlogn)    O(n)    out-place   stable      comparison
# quick     O(nlogn)    O(nlogn)    O(n^2)      O(logn) in-place    unstable    comparison
# heap      O(nlogn)    O(nlogn)    O(nlogn)    O(1)    in-place    unstable    comparison
# counting  O(n+k)      O(n+k)      O(n+k)      O(k)    out-place   stable      non-comparison
# bucket    O(n+k)      O(n+k)      O(n^2)      O(n+k)  out-place   stable      non-comparison
# radix     O(nk)       O(nk)       O(nk)       O(n+k)  out-place   stable      non-comparison

import random
import time
from collections import deque
from collections import defaultdict

'''
quick sort 
avg: O(nlogn), best: O(nlogn), worst: O(n^2), space: O(logn), in-place, unstable, comparison
fastest in large-scale and out-of-order data, divide & conquer
'''


def quick_sort(arr):
    quick_sort_rec(arr, 0, len(arr) - 1)


# hi is included, in range [lo, hi]
def quick_sort_rec(arr, lo, hi):
    if lo < hi:
        pivot = partition(arr, lo, hi)

        quick_sort_rec(arr, lo, pivot - 1)
        quick_sort_rec(arr, pivot + 1, hi)


def partition(arr, lo, hi):
    # choose pivot by median-of-three
    x, idx = sorted(((arr[lo], lo), (arr[hi], hi), (arr[lo + hi >> 1], lo + hi >> 1)))[1]
    arr[lo], arr[idx] = arr[idx], arr[lo]
    while lo < hi:
        while lo < hi and arr[hi] >= x:
            hi -= 1
        arr[lo] = arr[hi]
        while lo < hi and arr[lo] <= x:
            lo += 1
        arr[hi] = arr[lo]
    arr[lo] = x
    return lo


'''
merge sort
avg: O(nlogn), best: O(nlogn), worst: O(nlogn), space: O(n), out-place, stable, comparison
divide & conquer
'''


# the version with a fixed temp array
def merge_sort(arr):
    merge_sort_rec(arr, 0, len(arr) - 1, [0] * len(arr))


def merge_sort_rec(arr, first, last, temp):
    if first < last:
        mid = (first + last) // 2
        merge_sort_rec(arr, first, mid, temp)
        merge_sort_rec(arr, mid + 1, last, temp)
        merge(arr, first, mid, last, temp)


def merge(arr, first, mid, last, temp):
    i, j = first, mid + 1
    m, n = mid, last
    k = 0
    while i <= m and j <= n:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= m:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= n:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(k):
        arr[first + i] = temp[i]


def merge_sort2(arr):
    res = merge_sort_rec2(arr)
    for i in range(len(arr)):
        arr[i] = res[i]


def merge_sort_rec2(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_rec2(arr[:mid])
    right = merge_sort_rec2(arr[mid:])
    return merge1(left, right)


def merge1(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res


# more pythonic but slower
def merge2(left, right):
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    return res + (left or right)


# slowest
def merge3(left, right):
    res = []
    while left and right:
        if left[-1] > right[-1]:
            res.insert(0, left.pop())
        else:
            res.insert(0, right.pop())
    return (left or right) + res


'''
insert sort
avg: O(n^2), best: O(n), worst: O(n^2), space: O(1), in-place, stable, comparison
fast in small-scale and almost sorted data 
'''


def insert_sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = x


'''
bubble sort
avg: O(n^2), best:O(n), worst: O(n^2), space:O(1), in-place, stable, comparison
optimization: 
1. flag whether swap last round, if not, end sort
2. flag the last swap place, [last_swap, j] has been sorted, just skip it.
'''


# bubble the max to right most
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# optimization
def bubble_sort2(arr):
    i = len(arr) - 1
    while i > 0:
        last_swap = 0
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                last_swap = j
        # if last_swap=0, it means no swap in last round, end sort
        # [last_swap, i] has been sorted, start from last_swap
        i = last_swap


'''
selection sort
avg: O(n^2), best: O(n^2), worst: O(n^2), space: O(1), in-place, unstable, comparison
most stable in time cost, always O(n^2), and easy understanding, used in small scale data
'''


def selection_sort(arr):
    for i in range(len(arr)):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]


'''
heap sort
avg: O(nlogn), best: O(nlogn), worst: O(nlogn), space: O(1), in-place, unstable, comparison
not only a sort algorithm, this structure (priority queue) can do more thing.
'''


def heap_sort(arr):
    # build max heap
    for i in range(len(arr) // 2)[::-1]:
        heap_adjust(arr, i, len(arr))

    # adjust from last element
    for i in range(1, len(arr))[::-1]:
        # swap first with the last, make the right most is maximum
        arr[0], arr[i] = arr[i], arr[0]
        heap_adjust(arr, 0, i)


def heap_adjust(arr, i, n):
    cur = arr[i]
    while 2 * i + 1 < n:
        # get child index in heap
        child = 2 * i + 1

        # choose the larger child
        if child < n - 1 and arr[child + 1] > arr[child]:
            child += 1

        # if child is larger than parent, sift up
        if cur < arr[child]:
            arr[i], arr[child] = arr[child], cur
            i = child
        else:
            break


'''
shell sort
avg: O(nlogn), best: O(nlogn^2), worst: O(nlogn^2), space: O(1), in-place, unstable, comparison
improvement of insertion sort
'''


def shell_sort(arr):
    # Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1.
    gap = len(arr) // 2
    # loop over the gaps
    while gap > 0:
        # do the insertion sort
        for i in range(gap, len(arr)):
            val = arr[i]
            j = i
            while j >= gap and arr[j - gap] > val:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = val
        gap //= 2


'''
counting sort
avg: O(n+k), best:O(n+k), worst:O(n+k), space:O(k), out-place, stable, non-comparison
relatively concentrated values
'''


def counting_sort(arr):
    min_val, max_val = min(arr), max(arr)
    size = max_val - min_val + 1
    counter = [0] * size

    for i in range(len(arr)):
        counter[arr[i] - min_val] += 1

    idx = 0
    for i, v in enumerate(counter):
        # use slice assignment
        arr[idx:idx + v] = [i + min_val] * v
        idx += v


'''
bucket sort
avg: O(n+k), best:O(n+k), worst:O(n^2), space:O(n+k), out-place, stable, non-comparison
improvement of counting sort, usually used with hash 
'''
DEFAULT_BUCKET_SIZE = 5


def bucket_sort(arr, size=DEFAULT_BUCKET_SIZE):
    min_val, max_val = min(arr), max(arr)

    # initialize buckets
    count = (max_val - min_val) // size + 1
    buckets = [[] for _ in range(count)]

    # put values in buckets
    for i in range(len(arr)):
        buckets[(arr[i] - min_val) // size].append(arr[i])

    # sort buckets and place back into input array
    i = 0
    for bucket in buckets:
        insert_sort(bucket)
        # use slice assignment
        arr[i:i + len(bucket)] = bucket
        i += len(bucket)


# with hash
def bucket_sort2(arr):
    # get hash codes
    code = hashing(arr)
    buckets = [[] for _ in range(code[1])]
    # distribute data into buckets: O(n)
    for i in arr:
        x = re_hashing(i, code)
        buckets[x].append(i)

    i = 0
    # merge the buckets: O(n)
    for bucket in buckets:
        insert_sort(bucket)
        arr[i:i + len(bucket)] = bucket
        i += len(bucket)


def hashing(arr):
    return [max(arr), int(len(arr) ** 0.5)]


def re_hashing(i, code):
    return int(i / code[0] * (code[1] - 1))


'''
radix sort
avg: O(nk), best:O(nk), worst:O(nk), space:O(n+k), out-place, stable, non-comparison
improvement of counting sort
'''


def radix_sort(arr):
    radix = 10
    max_length = False
    placement = 1

    while not max_length:
        max_length = True
        # declare and initialize buckets
        buckets = [[] for _ in range(radix)]

        # split arr between lists
        for i in arr:
            temp = i // placement
            buckets[temp % radix].append(i)
            if max_length and temp > 0:
                max_length = False

        # assign from bucket to arr
        i = 0
        for bucket in buckets:
            insert_sort(bucket)
            # use slice assignment
            arr[i:i + len(bucket)] = bucket
            i += len(bucket)

        # move to next digit
        placement *= radix
    return arr


'''
topological sort
in a directed graph, a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, 
u comes before v in the ordering. 
'''

GRAY, BLACK = 0, 1


def topological_sort(graph):
    order, enter, state = deque(), set(graph), {}

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY:
                raise ValueError("cycle")
            if sk == BLACK:
                continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter:
        dfs(enter.pop())
    return order


if __name__ == '__main__':
    def sort_test(sort_func):
        start = time.time()
        for _ in range(100):
            nums = [random.randrange(1, 250) for _ in range(1000)]
            nums1 = sorted(nums)
            sort_func(nums)
            if nums1 != nums:
                print('incorrect', )
        end = time.time()
        print('{:15s} time: {}'.format(sort_func.__name__, end - start))


    sort_test(quick_sort)
    sort_test(merge_sort)
    sort_test(merge_sort2)
    sort_test(heap_sort)
    sort_test(shell_sort)
    sort_test(counting_sort)
    sort_test(bucket_sort)
    sort_test(bucket_sort2)
    sort_test(radix_sort)

    # put turtle algorithms to the tail
    sort_test(insert_sort)
    sort_test(bubble_sort)
    sort_test(bubble_sort2)
    sort_test(selection_sort)

    graph = defaultdict(list)
    graph['A'].append('B')
    graph['B'].append('D')
    graph['C'].append('A')
    print(topological_sort(graph))

```

### `16. 树和链表结合`
>36. 二叉搜索树与双向链表
>109. Convert Sorted List to Binary Search Tree
>114. Flatten Binary Tree to Linked List

```python3
# Classification: binary tree, complete binary tree, full binary tree, binary search tree, AVL tree(self-balancing)
#
# Time:  O(n)
# Space: O(h) h: height of tree
from collections import deque


# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
traverse binary tree recursively
'''


# pre-order: root->left->right
def preorder_traversal_recursively(self, root: 'TreeNode'):
    # recursion terminator here
    # you can check if none when add left and right child, it will decrease one recursion depth,
    # but you have to check whether root is None outside.
    if not root:
        return
    '''
    add current node logic here
    '''
    self.process_logic(root)

    self.preorder_traversal_recursively(root.left)
    self.preorder_traversal_recursively(root.right)


# in-order: left->root->right
def inorder_traversal_recursively(self, root: 'TreeNode'):
    if not root:
        return

    self.inorder_traversal_recursively(root.left)
    '''
    add current node logic here
    '''
    self.process_logic(root)

    self.inorder_traversal_recursively(root.right)


# post-order: left->right->root
def postorder_traversal_recursively(self, root: 'TreeNode'):
    if not root:
        return

    self.postorder_traversal_recursively(root.left)
    self.postorder_traversal_recursively(root.right)
    '''
    add current node logic here
    '''
    self.process_logic(root)


# level-order
# to traverse recursively, need help from extra data structure or dfs level by level
def level_order_traversal_recursively(self, root: 'TreeNode') -> 'List[List[int]]':
    res = []

    def dfs(root, level):
        if not root:
            return
        if len(res) < level + 1:
            res.append([])
        '''
        add current node logic here
        '''
        self.process_logic(root)

        res[level].append(root.val)
        dfs(root.left, level + 1)
        dfs(root.right, level + 1)

    dfs(root, 0)
    return res


'''
traverse binary tree iteratively
'''


# There are too many version to traverse iteratively, just choose the one you like it.
# pre-order: root->left->right
def preorder_traversal_iteratively(self, root: 'TreeNode'):
    if not root:
        return []
    stack = [root]
    while stack:
        root = stack.pop()
        '''
        add current node logic here
        '''
        self.process_logic(root)

        # push right child first because of FILO
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)


# in-order: left->root->right
def inorder_traversal_iteratively(self, root: 'TreeNode'):
    stack = []
    # keep stack empty and compare root too, compatible with edge case: root=None
    while stack or root:
        # push itself and all left children into stack iteratively
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        '''
        add current node logic here
        '''
        self.process_logic(root)

        # point to right child
        root = root.right


# here I choose to not use
# post-order: left->right->root
def postorder_traversal_iteratively(self, root: 'TreeNode'):
    if not root:
        return []
    stack = [root]
    # used to record whether left or right child has been visited
    last = None

    while stack:
        root = stack[-1]
        # if current node has no left right child, or left child or right child has been visited, then process and pop it
        if not root.left and not root.right or last and (root.left == last or root.right == last):
            '''
            add current node logic here
            '''
            self.process_logic(root)

            stack.pop()
            last = root
        # if not, push right and left child in stack
        else:
            # push right first because of FILO
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)


# post-order: left->right->root
# use visit flag
def postorder_traversal_iteratively2(self, root: 'TreeNode'):
    if not root:
        return []
    stack = [root]
    while stack:
        root = stack[-1]
        # use visited attribute to judge whether it has been visited
        if hasattr(root, 'visited'):
            '''
            add current node logic here
            '''
            self.process_logic(root)

            stack.pop()
            del root.visited
        else:
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            root.visited = True


# level-order
def level_order_traversal_iteratively(self, root: 'TreeNode'):
    if not root:
        return []
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            '''
            add current node logic here
            '''
            self.process_logic(cur)

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        '''
        add level logic here if you need
        '''
```


### `17. 树的重新构建`
>105. Construct Binary Tree from Preorder and Inorder Traversal
>106. Construct Binary Tree from Inorder and Postorder Traversal
>606. Construct String from Binary Tree
>1008. Construct Binary Search Tree from Preorder Traversal
>889. Construct Binary Tree from Preorder and Postorder Traversal

```python3
相关算法模板同上树和链表结合
```

### `18. 位运算`
>136. Single Number
>540. Single Element in a Sorted Array
>190. Reverse Bits
>* 剑指 Offer 15. 二进制中1的个数
>* 剑指 Offer 56 - I. 数组中数字出现的次数
>* 剑指 Offer 56 - II. 数组中数字出现的次数 II

```python3
# Bit manipulation is the act of algorithmically manipulating bits or other pieces of data shorter than a word.
#
# common bit-wise operation
#
# operations priority:
# {}[]() -> ** -> ~ -> -x -> *,/,% -> +,- -> <<,>> -> & -> ^ -> | -> <>!= -> is -> in -> not x -> and -> or


def bit_wise_operations(a, b):
    # not
    ~a

    # or
    a | b

    # and
    a & b

    # xor
    a ^ b

    # shift operators
    a << b
    a >> b

    # subtraction
    a & ~b

    # set bit, assign to 1
    a |= 1 << b

    # clear bit, assign to 0
    a &= ~(1 << b)

    # test bit
    if a & 1 << b: pass

    # extract last bit
    a & -a

    # remove last bit
    a & (a - 1)

    # check is odd or even
    if a & 1: print('odd')

    # clear right n bit
    a & (~0 << b)

    # clear left until to n
    a & ((1 << b) - 1)

# reference
# https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
```

### `19. 字符串`
>一般都有很多corner cases 需要考虑
>8. String to Integer (atoi)
>* 剑指 Offer 20. 表示数值的字符串
>* 剑指 Offer 58 - I. 翻转单词顺序(2次翻转）
>* 剑指 Offer 58 - II. 左旋转字符串

```python3
# string is traditionally a sequence of characters, either as a literal constant or as some kind of variable.
import string


def string_operations():
    s = 'abcab'

    # join
    ','.join(s)

    # split
    s.split(',')

    # replace
    s.replace()

    # index & find, index return -1 if not found
    s.index('a')
    s.find('a')
    s.rfind('a')

    # count
    s.count('a')

    # start & end with
    s.startswith('a')
    s.endswith('b')

    # translate
    intab = "aeiou"
    outtab = "12345"
    trantab = str.maketrans(intab, outtab)
    s.translate(trantab)

    # strip
    s.lstrip()
    s.rstrip()
    s.strip()

    # just
    s.ljust(10)
    s.rjust(10)
    s.center(10)
    s.zfill(10)

    # common string
    string.punctuation
    string.whitespace
    string.ascii_lowercase
    string.hexdigits
    string.printable
```


### `20. stack`

>* 剑指 Offer 31. 栈的压入、弹出序列

```python3
# stack common operation: push, pop, top
# stack is used in pairs, maintain extreme value
#
# FILO: First In, Last Out
# Time:  O(1)
# Space: O(n)


# sequence stack based on list
def stack_operations():
    # initialization
    stack = []

    # size of stack
    size = len(stack)

    # push
    stack.append(1)

    # check is empty
    if stack:
        # top
        top = stack[-1]

        # pop
        stack.pop()
```


### `21. array`
>* 剑指 Offer 66. 构建乘积数组
```python3

# list is a collection which is ordered and changeable, with continuous space.
#
# Time:  O(1) to index or write or append, O(n) to insert or remove
# Space: O(n)


def list_operations():
    # initialization
    list1 = [3, 1, 2, 4]

    list2 = list(range(5))
    # [*X] equals to list(X)
    list2 = [*range(5)]

    # append
    list1.append(5)
    list1 += [5]
    list1 += 5,
    list1.extend([5, 6])

    # insert
    list1.insert(0)

    # index
    list1.index(3)

    # count
    list1.count(3)

    # remove
    list1.remove(3)

    # sort
    list1.sort(reverse=True)

    # reverse
    list1.reverse()
```

### `22. 二叉搜索树`

>* 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
>* 剑指 Offer 68 - II. 二叉树的最近公共祖先
>* 二叉树的下一个结点

```python3

# binary search requires sorted iterator. Common variation is find left-most or right-most index.
#
# Time:  O(log(n))
# Space: O(1)


# [lo, hi] version
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        # no overflow problem in python, (lo + hi) // 2 is better.
        # mid = lo + (hi - lo) // 2
        mid = (lo + hi) // 2
        '''
        change to your comparison condition as you need
        '''
        # find the target
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1


# [lo, hi) version
def binary_search2(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        # find the target
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid


# result in [0, hi]
def bisect_left(arr, target, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        # left-most, so equal will be on the right side
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
        '''
        # bisect right code
        if arr[mid] > target:
            hi = mid
        else:
            lo = mid + 1
        '''
    return lo
```

### 算法和数据结构(学习相关书籍推荐)

>- 算法图解.pdf  [百度云下载链接](https://pan.baidu.com/s/1dhEy_uvJYoqehdvYnHzoBg)  密码:lk0v
>- 算法第四版.pdf  [百度云下载链接](https://pan.baidu.com/s/1b89HDicDLsCC_qg894FUvA)  密码:gsjc
>- 算法导论第三版.pdf  [百度云下载链接](https://pan.baidu.com/s/1ljP9Qwg5RqL_4LzrYK9jrA)  密码:qans
>- 数据结构与算法经典问题解析Java语言描述.pdf  [百度云下载链接](https://pan.baidu.com/s/1cXLrpad3Z-huk5otPVMMjg)  密码:m7ef
>- 数据结构与算法分析:C语言描述_原书第2版.pdf  [百度云下载链接](https://pan.baidu.com/s/1MudCT3RNO9I991surooqgg)  密码:1w5g
>- 大话数据结构.pdf  [百度云下载链接](https://pan.baidu.com/s/1dyH64h2603-ag8Yk6UM94w)  密码:h5du
>- 编程之美——微软技术面试心得.pdf  [百度云下载链接](https://pan.baidu.com/s/1r1VkAgh03G5Zfha35coyrg)  密码:rcpv
>- 编程之法.pdf  [百度云下载链接](https://pan.baidu.com/s/1jbypY-mQxJ1M1Hz97ptFjQ)  密码:0cv3
>- 背包九讲.pdf  [百度云下载链接](https://pan.baidu.com/s/13-ov__8xJ_SSxCmhkP4iSQ)  密码:he90
>- 啊哈算法.pdf  [百度云下载链接](https://pan.baidu.com/s/1vO9c3T3v89krlMsWEGDQCw)  密码:h89a
>- Algorithms, 4th Edition(算法，第四版).pdf  [百度云下载链接](https://pan.baidu.com/s/1ugDCe6ISRoa1Zi3UGW5Ncw)  密码:ipni
>- 《LeetCode101（谷歌师兄刷题笔记）》[百度网盘链接](https://pan.baidu.com/s/1PERa4bL7K-FoXit5440YNQ)  密码: 14fn
>- 《第二份谷歌刷题笔记》 [百度网盘链接](https://pan.baidu.com/s/1HMJvHjB964OpwtHAJQrPQw)  密码: k70j
>-  阿里霜神-《LeetCode刷题手册》 [百度网盘链接](https://pan.baidu.com/s/1817n69g0eOj7fptRpdR3kQ)  密码: fwtn


### Donate

如果本仓库对你有帮助，可以请作者喝杯速溶咖啡,给大家推荐个Google大佬的算法课程。
