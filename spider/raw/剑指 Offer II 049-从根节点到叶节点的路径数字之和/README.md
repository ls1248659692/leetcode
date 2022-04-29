# [从根节点到叶节点的路径数字之和][title]

## Description

给定一个二叉树的根节点 `root` ，树中每个节点都存放有一个 `0` 到 `9` 之间的数字。

每条从根节点到叶节点的路径都代表一个数字：

  * 例如，从根节点到叶节点的路径 `1 -> 2 -> 3` 表示数字 `123` 。

计算从根节点到叶节点生成的 **所有数字之和** 。

**叶节点** 是指没有子节点的节点。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg)
            **输入：** root = [1,2,3]    **输出：** 25    **解释：**    从根到叶子节点路径 1->2 代表数字 12    从根到叶子节点路径 1->3 代表数字 13    因此，数字总和 = 12 + 13 = 25

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg)
            **输入：** root = [4,9,0,5,1]    **输出：** 1026    **解释：**    从根到叶子节点路径 4->9->5 代表数字 495    从根到叶子节点路径 4->9->1 代表数字 491    从根到叶子节点路径 4->0 代表数字 40    因此，数字总和 = 495 + 491 + 40 = 1026    



**提示：**

  * 树中节点的数目在范围 `[1, 1000]` 内
  * `0 <= Node.val <= 9`
  * 树的深度不超过 `10`



注意：本题与主站 129 题相同： <https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/>


**Tags:** Tree, Depth-First Search, Binary Tree

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
    def sumNumbers(self, root: TreeNode) -> int:
        def trs_v2(nd,order,nullv,dd):
            #print(nd)
            if not nd:return [[nullv,dd]]
            elif not nd.left and not nd.right: res= [[nullv+[nd.val,'e'],dd+nd.val]]
            else:
                res= [[nullv+[nd.val],None]] + trs_v2(nd.left,order,nullv+[nd.val],dd+nd.val) + trs_v2(nd.right,order,nullv+[nd.val],dd+nd.val)
            return res        
        tli = trs_v2(root,'pre',[None],0)        
        print(tli)
        mli = [el[0] for el in tli if el[0][-1]=='e' ] 
        mli = [''.join([str(e) for e in r if e is not None and e!='e']) for r in mli]
        su = sum([int(e) for e in mli])
        print(mli)
        return su        
```

[title]: https://leetcode-cn.com/problems/3Etpl5
