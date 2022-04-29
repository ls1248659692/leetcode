# [Maximum Binary Tree II][title]

## Description

最大树定义：一个树，其中每个节点的值都大于其子树中的任何其他值。

给出最大树的根节点 `root`。

就像[之前的问题](https://leetcode-cn.com/problems/maximum-binary-tree/)那样，给定的树是从列表
`A`（`root = Construct(A)`）递归地使用下述 `Construct(A)` 例程构造的：

  * 如果 `A` 为空，返回 `null`
  * 否则，令 `A[i]` 作为 A 的最大元素。创建一个值为 `A[i]` 的根节点 `root`
  * `root` 的左子树将被构建为 `Construct([A[0], A[1], ..., A[i-1]])`
  * `root` 的右子树将被构建为 `Construct([A[i+1], A[i+2], ..., A[A.length - 1]])`
  * 返回 `root`

请注意，我们没有直接给定 A，只有一个根节点 `root = Construct(A)`.

假设 `B` 是 `A` 的副本，并在末尾附加值 `val`。题目数据保证 `B` 中的值是不同的。

返回 `Construct(B)`。

**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/02/23/maximum-binary-
tree-1-1.png)![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/02/23/maximum-binary-tree-1-2.png)**
            **输入：** root = [4,1,3,null,null,2], val = 5    **输出：** [5,4,null,1,3,null,null,2]    **解释：** A = [1,4,2,3], B = [1,4,2,3,5]    

**示例 2：  
![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/02/23/maximum-binary-
tree-2-1.png)![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/02/23/maximum-binary-tree-2-2.png)**
            **输入：** root = [5,2,4,null,1], val = 3    **输出：** [5,2,4,null,1,null,3]    **解释：** A = [2,1,5,4], B = [2,1,5,4,3]    

**示例 3：  
![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/02/23/maximum-binary-
tree-3-1.png)![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/02/23/maximum-binary-tree-3-2.png)**
            **输入：** root = [5,2,3,null,1], val = 4    **输出：** [5,2,4,null,1,3]    **解释：** A = [2,1,5,3], B = [2,1,5,3,4]    

**提示：**

  * `1 <= B.length <= 100`


**Tags:** Tree, Binary Tree

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
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        td = TreeNode(val)
        def trav(node,par):
            nonlocal root,td
            if td.left:return
            if not node: 
                par.right=td
                td.left=1
                return
            if node.val<val:
                td.left=node
                if not par: root= td
                if  par and par.left == node:par.left =td
                if  par and par.right == node:par.right =td
            else:
                trav(node.right,node)
                #trav(node.left,node)

        trav(root,None)
        if td.left==1: td.left=None
        return root
                

```

[title]: https://leetcode-cn.com/problems/maximum-binary-tree-ii
