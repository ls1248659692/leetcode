# [Average of Levels in Binary Tree][title]

## Description

给定一个非空二叉树的根节点 `root` , 以数组的形式返回每一层节点的平均值。与实际答案相差 `10-5` 以内的答案可以被接受。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg)
            **输入：** root = [3,9,20,null,null,15,7]    **输出：** [3.00000,14.50000,11.00000]    **解释：** 第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。    因此返回 [3, 14.5, 11] 。    

**示例 2:**

![](https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg)
            **输入：** root = [3,9,20,15,7]    **输出：** [3.00000,14.50000,11.00000]    



**提示：**

  * 树中节点数量在 `[1, 104]` 范围内
  * `-231 <= Node.val <= 231 - 1`


**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

**Difficulty:** Easy

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[order]+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val,order]+[dd*unit]]
            else:
                res= [[nd.val,order]+[dd]] + trs(nd.left,'r%d'%nd.val,nullv,dd+1) + trs(nd.right,'r%d'%nd.val,nullv,dd+1)
            return res        
        tli = trs(root,'r%d'%root.val,[None],1) 
        print(tli)

        dic = {}
        for tt in tli:
            dic.setdefault(tt[-1],[])
            if tt[0] is not None: dic[tt[-1]].append(tt[0])
        return [sum(el[1])/len(el[1]) for el in sorted(dic.items(),key=lambda xx:xx[0])]
```

[title]: https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
