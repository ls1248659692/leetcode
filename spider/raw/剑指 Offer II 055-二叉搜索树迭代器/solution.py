# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root= root
        self.stk=[]
        self.p=TreeNode('init')

    def next(self) -> int:
        r=-1
        if self.p is not None and self.p.val=='init':
            print('init')
            self.p=self.root
        if self.p or self.stk:
                while self.p and (self.stk.append(self.p) or self.p): self.p = self.p.left  
                self.p = self.stk.pop()
                r = self.p.val
                self.p = self.p.right 
        return r

    def hasNext(self) -> bool:
        return True if self.p or self.stk else False




# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()