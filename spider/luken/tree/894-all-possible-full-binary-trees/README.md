# [All Possible Full Binary Trees][title]

## Description

_满二叉树_ 是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。

返回包含 `N` 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。

答案中每个树的每个`结点`都 **必须** 有 `node.val=0`。

你可以按任何顺序返回树的最终列表。



**示例：**
            **输入：** 7    **输出：** [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]    **解释：**    ![](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/08/24/fivetrees.png)    



**提示：**

  * `1 <= N <= 20`


**Tags:** Tree, Recursion, Memoization, Dynamic Programming, Binary Tree

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
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n%2==0: return []
        # n1= [TreeNode(0)]
        # n3 = n1 + [TreeNode(0),TreeNode(0)]
        # n3[0].left,n3[0].right =n3[1],n3[1]
        # for n in n3:
        #     n+[TreeNode(0),TreeNode(0)]
        #     n7 3,3  2* (1,5_1a 1,5_1b)
        #     n9 4,4  2*(1,7 3,5)
        #     n11 5,5 2
        cache={}
        def fbt(n):
            if n in cache:return cache[n]
            if n==0: trLs= [None]
            elif n==1:trLs= [TreeNode(0)]
            else:
                trLs=[]
                for i in range(1,n-1,2):
                    for tree1 in fbt(i):
                        for tree2 in fbt(n-1-i):
                            td =TreeNode(0)
                            td.left,td.right=tree1,tree2
                            trLs.append(td)
            cache[n]=list(trLs)
            return trLs
        r=fbt(n)
        #print(cache)
        return r
```

[title]: https://leetcode-cn.com/problems/all-possible-full-binary-trees
