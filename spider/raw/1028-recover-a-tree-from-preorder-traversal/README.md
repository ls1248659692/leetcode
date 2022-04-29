# [Recover a Tree From Preorder Traversal][title]

## Description

我们从二叉树的根节点 `root` 开始进行深度优先搜索。

在遍历中的每个节点处，我们输出 `D` 条短划线（其中 `D` 是该节点的深度），然后输出该节点的值。（ _如果节点的深度为`D`，则其直接子节点的深度为
`D + 1`。根节点的深度为 `0`）。_

如果节点只有一个子节点，那么保证该子节点为左子节点。

给出遍历输出 `S`，还原树并返回其根节点 `root`。



**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/04/12/recover-a-tree-from-preorder-traversal.png)**
            **输入：** "1-2--3--4-5--6--7"    **输出：** [1,2,5,3,4,6,7]    

**示例 2：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/04/12/screen-shot-2019-04-10-at-114101-pm.png)**
            **输入：** "1-2--3---4-5--6---7"    **输出：** [1,2,5,3,null,6,null,4,null,7]    

**示例 3：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/04/12/screen-
shot-2019-04-10-at-114955-pm.png)
            **输入：** "1-401--349---90--88"    **输出：** [1,401,null,349,88,90]    



**提示：**

  * 原始树中的节点数介于 `1` 和 `1000` 之间。
  * 每个节点的值介于 `1` 和 `10 ^ 9` 之间。


**Tags:** Tree, Depth-First Search, String, Binary Tree

**Difficulty:** Hard

## 思路

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def dtree_v1(s):
            nli = ['']
            for i in range(len(s)):
                if s[i] =='-' and s[i-1]!='-':
                    nli.append('-')
                else:
                    nli[-1] += s[i]
            return nli
        rg=lambda x,n:list(range(x,x+n))
        m4 = lambda md:[md,md-1,md,md]
        dt = dtree_v1(traversal)
        dt = [[el.count('-'),int(el.replace('-',''))]for el in dt]
        md= max([el[0]for el in dt])
        nli=[0]*md
        print('maxdepth.0->%sth nodenum=%s'%(md,len(dt)))

        root= TreeNode(dt[0][1])
        for i in range(1,len(dt)):
            depth,val=dt[i]
            for n in range(depth,md):nli[n]=0
            nli[depth-1]+=1
            print(val,depth,nli)
            node =root
            for dd in range(depth-1): node = node.left if nli[dd]%2  else node.right
            if nli[depth-1]%2 :node.left=TreeNode(val) 
            else: node.right=TreeNode(val)
        return root
```

[title]: https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal
