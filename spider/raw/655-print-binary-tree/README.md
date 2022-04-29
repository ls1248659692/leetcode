# [Print Binary Tree][title]

## Description

在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：

  1. 行数 `m` 应当等于给定二叉树的高度。
  2. 列数 `n` 应当总是奇数。
  3. 根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（ **左下部分和右下部分** ）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。
  4. 每个未使用的空间应包含一个空的字符串`""`。
  5. 使用相同的规则输出子树。

**示例 1:**
            **输入:**         1        /       2    **输出:**    [["", "1", ""],     ["2", "", ""]]    

**示例 2:**
            **输入:**         1        / \       2   3        \         4    **输出:**    [["", "", "", "1", "", "", ""],     ["", "2", "", "", "", "3", ""],     ["", "", "4", "", "", "", ""]]    

**示例 3:**
            **输入:**          1         / \        2   5       /       3      /     4     **输出:**    [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]     ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]     ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]     ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]    

**注意:** 二叉树的高度在范围 [1, 10] 中。


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
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def v2(node):
            res,que=[['.']],[[node,1,'-']]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                que.append([node.left,h+1,path+'L'])
                que.append([node.right,h+1,path+'R'])  
                res[h].append(path+':'+str(node.val))
            return res #[:-1] if len(res)>=2 else res
        r=  v2(root)
        print(r,len(r))
        ht= len(r)-1
        g=[['']*(2**ht-1) for i in range(ht)]
        print(g)
        for i in range(1,len(r)):
            for nd in r[i]:
                path,val = nd.split(':')
                path = path.replace('L','0').replace('R','1').replace('-','')
                #print(path)
                if not path: 
                    t= (int('0',base=2)*2**(ht+1-i)+ 2**(ht-i)-1)  #1
                else:
                    t=int(path,base=2)*2**(ht+1-i)+ 2**(ht-i)-1
                print(t)
                if val:g[i-1][t]=val
                    # if i==2:print(int(path,base=2)*2**(ht+1-i)+ 2**(ht-i)-1)
                    # if i==3: print(int(path,base=2)*2**(ht+1-i)+ 2**(ht-i)-1)
                    # if i==4: print('h4',int(path,base=2)*2**(ht+1-i)+ 2**(ht-i)-1)
                #print(t,val)
        return g
```

[title]: https://leetcode-cn.com/problems/print-binary-tree
