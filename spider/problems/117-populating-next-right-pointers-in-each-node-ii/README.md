# [Populating Next Right Pointers in Each Node II][title]

## Description

给定一个二叉树
            struct Node {      int val;      Node *left;      Node *right;      Node *next;    }

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 `NULL`。

初始状态下，所有 next 指针都被设置为 `NULL`。

**进阶：**

  * 你只能使用常量级额外空间。
  * 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

**示例：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/02/15/117_sample.png)
            **输入** ：root = [1,2,3,4,5,null,7]    **输出：** [1,#,2,3,#,4,5,7,#]    **解释：** 给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。

**提示：**

  * 树中的节点数小于 `6000`
  * `-100 <= node.val <= 100`


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
    def connect(self, root: 'Node') -> 'Node':
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
        return root        
```

[title]: https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
