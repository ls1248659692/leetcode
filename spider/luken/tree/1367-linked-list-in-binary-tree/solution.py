# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def v2b(node):
            res,leaf,que=[[[node.val]]],[],[[node,1,[]]]
            while que:
                node,h,path =que.pop(0)
                if not node:continue
                while h>=len(res):res.append([])
                que.append([node.left,h+1,path+[node.val]])
                que.append([node.right,h+1,path+[node.val]])  
                pa = path+[node.val,'e'] if not node.right and not node.left else  path+[node.val]
                res[h].append(pa)
                if not node.right and not node.left: leaf.append(pa)
            return leaf
        leaf= v2b(root)     
        lnkls=[]
        while head and (lnkls.append(head.val) or head): head=head.next

        def issubls(ls1,ls2):
            if len(ls2)>len(ls1):return False
            for i1 in range(len(ls1)-len(ls2)):
                if ls1[i1:i1+len(ls2)]==ls2:return True
            return False

        for pa in leaf:
            if issubls(pa,lnkls):return True
        return False