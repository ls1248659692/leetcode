# [Add One Row to Tree][title]

## Description

给定一个二叉树的根 `root` 和两个整数 `val` 和 `depth` ，在给定的深度 `depth` 处添加一个值为 `val` 的节点行。

注意，根节点 `root` 位于深度 `1` 。

加法规则如下:

  * 给定整数 `depth`，对于深度为 `depth - 1` 的每个非空树节点 `cur` ，创建两个值为 `val` 的树节点作为 `cur` 的左子树根和右子树根。
  * `cur` 原来的左子树应该是新的左子树根的左子树。
  * `cur` 原来的右子树应该是新的右子树根的右子树。
  * 如果 `depth == 1 `意味着 `depth - 1` 根本没有深度，那么创建一个树节点，值 `val `作为整个原始树的新根，而原始树就是新根的左子树。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/03/15/addrow-tree.jpg)
            **输入:** root = [4,2,6,3,1,5], val = 1, depth = 2    **输出:** [4,1,1,2,null,null,6,3,1,5]

**示例 2:**

![](https://assets.leetcode.com/uploads/2021/03/11/add2-tree.jpg)
            **输入:** root = [4,2,null,3,1], val = 1, depth = 3    **输出:**  [4,2,null,1,1,3,null,null,1]    



**提示:**

  * 节点数在 `[1, 104]` 范围内
  * 树的深度在 `[1, 104]`范围内
  * `-100 <= Node.val <= 100`
  * `-105 <= val <= 105`
  * `1 <= depth <= the depth of tree + 1`


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        def v2b(node):
            res,leaf,que=[[[node]]],[],[[node,1,None,'-']]
            while que:
                node,h,par,pd =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                que.append([node.left,h+1, node, 'L'])
                que.append([node.right,h+1,node,'R'])  
                pa =  path+[node]
                res[h].append([node,par,pd])
                if not node.right and not node.left: leaf.append(pa)
            return res

        res= v2b(root)   
        print('len_r=%s'%len(res))
        print([[e[0].val for e in h] for h in res[1:]])
        tli=[]
        if depth==1:
            td= TreeNode(val)
            td.left=root
            return td
        elif depth == len(res):
            for nd,par,pd in res[depth-1]:
                td = TreeNode(val)
                tli.append(td)
                nd.left=td
                td = TreeNode(val)
                tli.append(td)                
                nd.right=td
            return root            
        else:
            for nd,par,pd in res[depth-1]:
                td = TreeNode(val)
                tli.append([td,nd,'L'])
                nd.left=td
                td = TreeNode(val)
                tli.append([td,nd,'R'])                
                nd.right=td

            for nd,par,pd in res[depth]:
                for td_,par_,pd_ in tli:
                    if par==par_ and pd_==pd:
                        if pd=='L':
                            td_.left = nd
                        else:
                            td_.right=nd
                        break

            return root
```

[title]: https://leetcode-cn.com/problems/add-one-row-to-tree
