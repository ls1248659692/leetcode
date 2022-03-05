# [Populating Next Right Pointers in Each Node][title]

## Description

给定一个  **完美二叉树  **，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
            struct Node {      int val;      Node *left;      Node *right;      Node *next;    }

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 `NULL`。

初始状态下，所有 next 指针都被设置为 `NULL`。



**示例 1：**

![](https://assets.leetcode.com/uploads/2019/02/14/116_sample.png)
            **输入：** root = [1,2,3,4,5,6,7]    **输出：** [1,#,2,3,#,4,5,6,7,#]    **解释：** 给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。    

**示例 2:**
            **输入：** root = []    **输出：** []    



**提示：**

  * 树中节点的数量在 `[0, 212 - 1]` 范围内
  * `-1000 <= node.val <= 1000`



**进阶：**

  * 你只能使用常量级额外空间。
  * 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。


**Tags:** Tree, Depth-First Search, Breadth-First Search, Linked List, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        unt =1
        def trs_he(nd,order,nullv,dd):
            if not nd:return [[dd,nullv[0]]]
            elif not nd.left and not nd.right: res= [[dd*unt,nd]]
            else:
                res= [[dd,nd]] + trs_he(nd.left,order,nullv,dd+1) + trs_he(nd.right,order,nullv,dd+1)
            #print(nd,res)
            return res        

        tli = trs_he(root,'pre',[None],1)
        print('...tli=%s'%tli)
        dic = {}
        for tt in tli:
            dic.setdefault(tt[0],[])
            if tt[1] is not None: dic[tt[0]].append(tt[1])
        #print(dic)
        for he,nodes in dic.items():
            for i in range(len(nodes)):
                #print(i,len(nodes))
                nodes[i].next= nodes[i+1] if i<len(nodes)-1 else None

        # if not root:return []
        return root
```

[title]: https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node
