# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        def v1(node):
            res,que=[[node.val]],[[node,1]]
            while que:
                node,h =que.pop(0)
                while h>=len(res):res.append([])
                if node.left: 
                    res[h].append(node.left.val)
                    que.append([node.left,h+1])
                if node.right:
                    res[h].append(node.right.val)
                    que.append([node.right,h+1])  
            return res[:-1]           
        res = v1(tree)
        print(res)
        ln = [[ListNode(v) for v in ar] for ar in res]
        #print(ln)
        for i in range(len(ln)):
            for j in range(len(ln[i])-2,-1,-1):
                ln[i][j].next= ln[i][j+1]
        return [ar[0] for ar in ln]