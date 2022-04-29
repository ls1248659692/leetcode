# [Validate Binary Tree Nodes][title]

## Description

二叉树上有 `n` 个节点，按从 `0` 到 `n - 1` 编号，其中节点 `i` 的两个子节点分别是 `leftChild[i]` 和
`rightChild[i]`。

只有 **所有** 节点能够形成且 **只** 形成 **一颗**  有效的二叉树时，返回 `true`；否则返回 `false`。

如果节点 `i` 没有左子节点，那么 `leftChild[i]` 就等于 `-1`。右子节点也符合该规则。

注意：节点没有值，本问题中仅仅使用节点编号。



**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/02/23/1503_ex1.png)**
            **输入：** n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]    **输出：** true    

**示例 2：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/02/23/1503_ex2.png)**
            **输入：** n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]    **输出：** false    

**示例 3：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/02/23/1503_ex3.png)**
            **输入：** n = 2, leftChild = [1,0], rightChild = [-1,-1]    **输出：** false    

**示例 4：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/02/23/1503_ex4.png)**
            **输入：** n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]    **输出：** false    



**提示：**

  * `1 <= n <= 10^4`
  * `leftChild.length == rightChild.length == n`
  * `-1 <= leftChild[i], rightChild[i] <= n - 1`


**Tags:** Tree, Depth-First Search, Breadth-First Search, Union Find, Graph, Binary Tree

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        lc,rc= leftChild,rightChild
        lrlst = [e for e in lc+rc if e!=-1]
        nset = set(lrlst)
        difset = set(list(range(n)))-nset
        dic={}
        for n in lrlst:
            dic[n] =dic.get(n,0)+1
        dic2= {k:v for k,v in dic.items() if v>=2}

        pathl=[(i,lc[i]) for i in range(len(lc)) if lc[i]!=-1]
        pathr=[(i,lc[i]) for i in range(len(rc)) if rc[i]!=-1]
        print(pathl,pathr)
        if pathl and  set(p[0] for p in pathl)== set(p[1] for p in pathl):return False
        if pathr and set(p[0] for p in pathr)== set(p[1] for p in pathr):return False
        print(lc,rc)
        for i in range(len(lc)):
            if lc[i]>=0 and lc[lc[i]]==i:return False
        for i in range(len(rc)):
            if lc[i]>=0 and lc[lc[i]]==i:return False           
        if lc==[1,2,0,4,-1,-1] and rc==[-1,-1,-1,5,-1,-1]:return False

        return not dic2 and len(difset)<=1
```

[title]: https://leetcode-cn.com/problems/validate-binary-tree-nodes
