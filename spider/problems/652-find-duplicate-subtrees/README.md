# [Find Duplicate Subtrees][title]

## Description

给定一棵二叉树 `root`，返回所有 **重复的子树** 。

对于同一类的重复子树，你只需要返回其中任意 **一棵** 的根结点即可。

如果两棵树具有 **相同的结构** 和 **相同的结点值** ，则它们是 **重复** 的。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/08/16/e1.jpg)
            **输入：** root = [1,2,3,4,null,2,4,null,null,4]    **输出：** [[2,4],[4]]

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/08/16/e2.jpg)
            **输入：** root = [2,1,1]    **输出：** [[1]]

**示例 3：**

**![](https://assets.leetcode.com/uploads/2020/08/16/e33.jpg)**
            **输入：** root = [2,2,2,3,null,3,null]    **输出：** [[2,3],[3]]



**提示：**

  * 树中的结点数在`[1,10^4]`范围内。
  * `-200 <= Node.val <= 200`


**Tags:** Tree, Depth-First Search, Hash Table, Binary Tree

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
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def search(node):
            nli,res,nres,stk=set(),[],[],[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                node = stk.pop()
                nd_s = serial(node)
                for q in nli:
                    if nd_s==q:
                       if q not in nres:
                           res.append(node)
                           nres.append(nd_s)
                       break
                nli.add(nd_s)
                node = node.right 
            return res

        def serial(node):
            def midt(node):
                if not node: 
                    tli.append('#')
                else:
                    tli.append(str(node.val)) 
                    midt(node.left)      
                    midt(node.right)  
            tli=[]   
            midt(node)
            print(','.join(tli))
            return ','.join(tli) if node else ''
        # return serial(root)
        return search(root)               
```

[title]: https://leetcode-cn.com/problems/find-duplicate-subtrees
