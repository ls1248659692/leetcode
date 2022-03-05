# [Linked List in Binary Tree][title]

## Description

给你一棵以 `root` 为根的二叉树和一个 `head` 为第一个节点的链表。

如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 `head` 为首的链表中每个节点的值，那么请你返回 `True` ，否则返回
`False` 。

一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。



**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/02/29/sample_1_1720.png)**
            **输入：** head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]    **输出：** true    **解释：** 树中蓝色的节点构成了与链表对应的子路径。    

**示例 2：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/02/29/sample_2_1720.png)**
            **输入：** head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]    **输出：** true    

**示例 3：**
            **输入：** head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]    **输出：** false    **解释：** 二叉树中不存在一一对应链表的路径。    



**提示：**

  * 二叉树和链表中的每个节点的值都满足 `1 <= node.val <= 100` 。
  * 链表包含的节点数目在 `1` 到 `100` 之间。
  * 二叉树包含的节点数目在 `1` 到 `2500` 之间。


**Tags:** Tree, Depth-First Search, Breadth-First Search, Linked List, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def v2b(node):
            res,leaf,que=[[[node.val]]],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                que.append([node.left,h+1,path+[node.val]])
                que.append([node.right,h+1,path+[node.val]])  
                pa = path+[node.val,'e'] if not node.right and not node.left else  path+[node.val]
                res[h].append(pa)
                if not node.right and not node.left: leaf.append(pa)
            return leaf
        leaf= v2b(root)     
        lnkls=[]
        while head and (lnkls.append(head.val) or head): head=head.next

        def issubls(ls1,ls2):
            if len(ls2)>len(ls1):return False
            for i1 in range(len(ls1)-len(ls2)):
                if ls1[i1:i1+len(ls2)]==ls2:return True
            return False

        for pa in leaf:
            if issubls(pa,lnkls):return True
        return False
```

[title]: https://leetcode-cn.com/problems/linked-list-in-binary-tree
