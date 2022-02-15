## 你将获得
      20 个经典数据结构与算法；

      100 个真实项目场景案例；

      文科生都能懂的算法手绘图解；

      轻松搞定 BAT 的面试通关秘籍。

## 专栏分为 4 个由浅入深的模块。

# `入门篇`
为什么要学习数据结构与算法？数据结构与算法该怎么学？学习的重点又是什么？这一模块将为你指明数据结构与算法的学习路径；并着重介绍贯穿整个专栏学习的重要概念：时间复杂度和空间复杂度，为后面的学习打好基础。

# `基础篇`
将介绍最常见、最重要的数据结构与算法。每种都从“来历”“特点”“适合解决的问题”“实际的应用场景”出发，进行详细介绍；并配有清晰易懂的手绘图解，由浅入深进行讲述；还适时总结一些实用“宝典”，教你解决真实开发问题的思路和方法。

# `高级篇`
将从概念和应用的角度，深入剖析一些稍复杂的数据结构与算法，推演海量数据下的算法问题解决过程；帮你更加深入理解算法精髓，开拓视野，训练逻辑；真正带你升级算法思维，修炼深厚的编程内功。

# `实战篇`
将通过实战案例串讲前面讲到的数据结构和算法；并拿一些开源项目和框架，剖析它们背后的数据结构和算法；并带你用学过的内容实现一个短网址系统；深化对概念和应用的理解，灵活使用数据结构和算法。


# 算法题汇总

  ## 不同算法类型
        1. 滑动窗口
        2. 双指针
        3. 快慢指针/ 链表题目
        4. 原地链表翻转
        5. 区间合并
        6. 无序限定范围的数组元素查找O(N）
        7. BFS
        8. 树的DFS
        9. DFS/递归/回溯法
        10. 双堆模式
        11. 2分变种
        12. 前K大的数模式HEAP
        13. K路归并
        14. DP 动态规划
        15. 排序算法
        16. 树和链表结合
        17. 树的重新构建
        18. 位运算
        19. 字符串
        20. stack
        21. math
        22. array
        23. 二叉搜索树

# 题型汇总

# `1. 滑动窗口`
    53. 大小为 K 的子数组的最大和
    121. Best Time to Buy and Sell Stock
    3. Longest Substring Without Repeating Characters
    239. Sliding Window Maximum
    剑指 Offer 57 - II. 和为s的连续正数序列

# `2. 双指针`
    双指针通常用在排好序的数组或是链表中寻找对子, 或者是merge 或者是排序，或者去除element，反正一般都是头尾各一个指针，然后根据条件移动。【参考Jaylen's Blog】 1. Two Sum（# 也可以用map的方式做）
    167. Two Sum II - Input array is sorted
    977. Squares of a Sorted Array (很像merge sort里的merge）
    283. Move Zeroes
    27. Remove Element
    26. Remove Duplicates from Sorted Array
    16. 3Sum Closest
    18. 4Sum
    86. Partition List
    11. Container With Most Water
    42. Trapping Rain Water
    75. Sort Colors
    剑指 Offer 04. 二维数组中的查找
    剑指 Offer 21. 调整数组顺序使奇数位于偶数前面

# `3. 快慢指针/ 链表题目`
    快慢指针是处理linked list常用的套路，通常是用来判断成环以及环的入口，或者是寻找 list中第k个元素。
    141. Linked List Cycle
    142. Linked List Cycle II
    234. Palindrome Linked List
    61. Rotate List
    剑指 Offer 18. 删除链表的节点
    JZ56 删除链表中重复的结点
    剑指 Offer 22. 链表中倒数第k个节点
    剑指 Offer 52. 两个链表的第一个公共节点

# `4. 原地链表翻转`
    234. Palindrome Linked List
    206. Reverse Linked List
    25. Reverse Nodes in k-Group
    92. Reverse Linked List II

# `5. 区间合并`
    区间合并的问题，通常是重新把区间按照start和end排序，重新组合区间。
    56. Merge Intervals
    986. Interval List Intersections
    57. Insert Interval

# `6. 无序限定范围的数组元素查找O(N）`
    要求 inplace， 通常是采用正负反转的做法
    41. First Missing Positive
    448. Find All Numbers Disappeared in an Array
    剑指 Offer 03. 数组中重复的数字

# `7. BFS`
    BFS 通常采用queue 来实现
    102. Binary Tree Level Order Traversal
    103. Binary Tree Zigzag Level Order Traversal
    297. Serialize and Deserialize Binary Tree
    127. Word Ladder I
    207. Course Schedule【拓扑排序】

# `8. 树的DFS`
    通常采用递归 111. Minimum Depth of Binary Tree
    112. Path Sum
    113. Path Sum II（和剑指 Offer 34. 二叉树中和为某一值的路径一样）
    437. Path Sum III
    100. Same Tree
    101. Symmetric Tree
    104. Maximum Depth of Binary Tree
    110. Balanced Binary Tree
    剑指 Offer 26. 树的子结构
    剑指 Offer 33. 二叉搜索树的后序遍历序列
    剑指 Offer 54. 二叉搜索树的第k大节点(inorder)

# `9. DFS/递归/回溯法`
    对于排列和组合的题目，需要主要判断是否会有重复数字，如有重复，需要先进行sort，而且需要进行剪枝。
    78. Subsets
    90. Subsets II
    46. Permutations
    47. Permutations II
    39. Combination Sum
    322. Coin Change
    518. Coin Change 2
    40. Combination Sum II
    131. Palindrome Partitioning !
    17. Letter Combinations of a Phone Number (differ from 91. Decode Ways)
    79. Word Search(same as 剑指 Offer 12. 矩阵中的路径)
    剑指 Offer 13. 机器人的运动范围
    10. 双堆模式
    295 Find-Median-from-Data-Stream
    480. Sliding Window Median
    155. Min Stack
    剑指 Offer 09. 用两个栈实现队列

# `11. 2分变种`
    当你需要解决的问题的输入是排好序的数组，链表，或是排好序的矩阵，要求咱们寻找某些特定元素。这个时候的不二选择就是二分搜索。这种模式是一种超级牛的用二分来解决问题的方式。 对于一组满足上升排列的数集来说，这种模式的步骤是这样的： 首先，算出左右端点的中点。最简单的方式是这样的：middle = (start + end) / 2。但这种计算方式有不小的概率会出现整数越界。因此一般都推荐另外这种写法：middle = start + (end — start) // 2 如果要找的目标改好和中点所在的数值相等，我们返回中点的下标就行 如果目标不等的话：我们就有两种移动方式了 如果目标比中点在的值小（key < arr[middle]）：将下一步搜索空间放到左边（end = middle - 1） 如果比中点的值大，则继续在右边搜索，丢弃左边：left = middle + 1 图示该过程的话，如下图所示： 我习惯的循环结束条件是 $start + 1 < end$（如果使用start=mid或者end=mid而不是+-1时必须要使用，否则可能进入死循环）, 然后在分别判断start 和 end 的结果 参考Jaylen's Blog 参考模版
    35. Search Insert Position
    34. Find First and Last Position of Element in Sorted Array
    33. Search in Rotated Sorted Array
    153. Find Minimum in Rotated Sorted Array
    154. Find Minimum in Rotated Sorted Array II(same as [剑指 Offer 11. 旋转数组的最小数字])
    162. Find Peak Element
    540. Single Element in a Sorted Array
    剑指 Offer 16. 数值的整数次方(2分法)

# `12. 前K大的数模式HEAP`
    采用priority queue 或者 说在python 中的heapq 求top k 采用最小堆（默认） 采用最大堆的时候可以采用push 负的value
    215. Kth Largest Element in an Array
    347. Top K Frequent Elements
    373. Find K Pairs with Smallest Sums

# `13. K路归并`
    K路归并能帮咱们解决那些涉及到多组排好序的数组的问题。
    每当你的输入是K个排好序的数组，你就可以用堆来高效顺序遍历其中所有数组的所有元素。你可以将每个数组中最小的一个元素加入到最小堆中，从而得到全局最小值。当我们拿到这个全局最小值之后，再从该元素所在的数组里取出其后面紧挨着的元素，加入堆。如此往复直到处理完所有的元素。
    特殊情况：2路并归 （mergesort 中的merge， 双指针就可以完成）
    23. Merge k Sorted Lists
    21. Merge Two Sorted Lists

# `14. DP 动态规划`
    300. Longest Increasing Subsequence
    1143. Longest Common Subsequence
    72. Edit Distance
    44. Wildcard Matching
    10. Regular Expression Matching
    120. Triangle
    53. Maximum Subarray
    152. Maximum Product Subarray
    887. Super Egg Dropref
    198. House Robber
    213. House Robber II (两个dp）
    121. Best Time to Buy and Sell Stock
    122. Best Time to Buy and Sell Stock II
    188. Best Time to Buy and Sell Stock IV
    123. Best Time to Buy and Sell Stock III ref
    714. Best Time to Buy and Sell Stock with Transaction Fee
    309. Best Time to Buy and Sell Stock with Cooldown
    516. Longest Palindromic Subsequence !
    5. Longest Palindromic Substring
    416. Partition Equal Subset Sum
    322. Coin Change
    518. Coin Change 2
    91. Decode Ways
    139. Word Break
    剑指 Offer 10- I. 斐波那契数列
    剑指 Offer 10- II. 青蛙跳台阶问题
    矩形覆盖
    变态跳台阶
    剑指 Offer 14- I. 剪绳子
    剑指 Offer 46. 把数字翻译成字符串
    剑指 Offer 47. 礼物的最大价值
    剑指 Offer 49. 丑数
    剑指 Offer 60. n个骰子的点数

# `15. 排序算法`
    Selection Sort
    Heapsort
    Mergesort
    Insertion Sort
    Shell's Sort
    Quicksort
    Bubblesort
    Linear Sorting

# `16. 树和链表结合`
    剑指 Offer 36. 二叉搜索树与双向链表
    109. Convert Sorted List to Binary Search Tree
    114. Flatten Binary Tree to Linked List

# `17. 树的重新构建`
    105. Construct Binary Tree from Preorder and Inorder Traversal
    106. Construct Binary Tree from Inorder and Postorder Traversal
    606. Construct String from Binary Tree
    1008. Construct Binary Search Tree from Preorder Traversal
    889. Construct Binary Tree from Preorder and Postorder Traversal

# `18. 位运算`
    136. Single Number
    540. Single Element in a Sorted Array
    190. Reverse Bits
    剑指 Offer 15. 二进制中1的个数
    剑指 Offer 56 - I. 数组中数字出现的次数
    剑指 Offer 56 - II. 数组中数字出现的次数 II

# `19. 字符串`
    一般都有很多corner cases 需要考虑 8. String to Integer (atoi)
    剑指 Offer 20. 表示数值的字符串
    剑指 Offer 58 - I. 翻转单词顺序(2次翻转）
    剑指 Offer 58 - II. 左旋转字符串

# `20. stack`
    剑指 Offer 31. 栈的压入、弹出序列

# `21. math`
    172. Factorial Trailing Zeroes
    470. Implement Rand10() Using Rand7()

# `22. array`
    剑指 Offer 66. 构建乘积数组

# `23. 二叉搜索树`
    剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
    剑指 Offer 68 - II. 二叉树的最近公共祖先
    二叉树的下一个结点
