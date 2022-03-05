# [Complete Binary Tree Inserter][title]

## Description

**完全二叉树** 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。

实现 `CBTInserter` 类:

  * `CBTInserter(TreeNode root)` 使用头节点为 `root` 的给定树初始化该数据结构；
  * `CBTInserter.insert(int v)`  向树中插入一个值为 `Node.val == val`的新节点 `TreeNode`。使树保持完全二叉树的状态， **并返回插入节点**  `TreeNode`  **的父节点的值** ；
  * `CBTInserter.get_root()` 将返回树的头节点。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/08/03/lc-treeinsert.jpg)
            **输入**    ["CBTInserter", "insert", "insert", "get_root"]    [[[1, 2]], [3], [4], []]    **输出**    [null, 1, 2, [1, 2, 3, 4]]        **解释**    CBTInserter cBTInserter = new CBTInserter([1, 2]);    cBTInserter.insert(3);  // 返回 1    cBTInserter.insert(4);  // 返回 2    cBTInserter.get_root(); // 返回 [1, 2, 3, 4]



**提示：**

  * 树中节点数量范围为 `[1, 1000]` 
  * `0 <= Node.val <= 5000`
  * `root` 是完全二叉树
  * `0 <= val <= 5000` 
  * 每个测试用例最多调用 `insert` 和 `get_root` 操作 `104` 次


**Tags:** Tree, Breadth-First Search, Design, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root= root
        self.ht = self.calcht()
        print('ht=',self.ht)

    def calcht(self,lr='l'):
        ht = 1
        nd =self.root
        while nd.left if lr=='l' else nd.right: 
            ht+=1
            nd= nd.left if lr=='l' else nd.right
            
        return ht

    def last(self):
        if self.calcht('r')==self.ht:
            nd =self.root
            while nd.left: 
                nd= nd.left          
            #print(nd)     
            return nd

        def trv(node,h,par):
            if tli:return
            #print(node.val if node else None, h)
            if not node: 
                return
            elif not node.right and not node.left:
                if h==self.ht: 
                    tli.append(node)
                if h==self.ht-1:ndli.append(node)                    
            else:
                trv(node.right,h+1,node)  
                if tli:return
                if h==self.ht-1:ndli.append(node)
                trv(node.left,h+1,node)   

        ndli,tli=[],[]   
        trv(self.root,1,None)
        #print('trv ht=%s ndli=%s'%(self.ht,ndli))
             
        return ndli[-1] 

    def insert(self, val: int) -> int:
        td =TreeNode(val)
        lastnd= self.last()

        if lastnd.left is None:
            lastnd.left = td
        else:
            lastnd.right =td

        self.ht=self.calcht('l')
        #print(self.root)
        return lastnd.val

    def get_root(self) -> TreeNode:
        return self.root

```

[title]: https://leetcode-cn.com/problems/complete-binary-tree-inserter
