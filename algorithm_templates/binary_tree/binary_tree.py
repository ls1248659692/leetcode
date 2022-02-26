# Classification: binary tree, complete binary tree, full binary tree, binary search tree, AVL tree(self-balancing)
#
# Time:  O(n)
# Space: O(h) h: height of tree
from collections import deque


# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
traverse binary tree recursively
'''


# pre-order: root->left->right
def preorder_traversal_recursively(self, root: 'TreeNode'):
    # recursion terminator here
    # you can check if none when add left and right child, it will decrease one recursion depth,
    # but you have to check whether root is None outside.
    if not root:
        return
    '''
    add current node logic here
    '''
    self.process_logic(root)

    self.preorder_traversal_recursively(root.left)
    self.preorder_traversal_recursively(root.right)


# in-order: left->root->right
def inorder_traversal_recursively(self, root: 'TreeNode'):
    if not root:
        return

    self.inorder_traversal_recursively(root.left)
    '''
    add current node logic here
    '''
    self.process_logic(root)

    self.inorder_traversal_recursively(root.right)


# post-order: left->right->root
def postorder_traversal_recursively(self, root: 'TreeNode'):
    if not root:
        return

    self.postorder_traversal_recursively(root.left)
    self.postorder_traversal_recursively(root.right)
    '''
    add current node logic here
    '''
    self.process_logic(root)


# level-order
# to traverse recursively, need help from extra data structure or dfs level by level
def level_order_traversal_recursively(self, root: 'TreeNode') -> 'List[List[int]]':
    res = []

    def dfs(root, level):
        if not root:
            return
        if len(res) < level + 1:
            res.append([])
        '''
        add current node logic here
        '''
        self.process_logic(root)

        res[level].append(root.val)
        dfs(root.left, level + 1)
        dfs(root.right, level + 1)

    dfs(root, 0)
    return res


'''
traverse binary tree iteratively
'''


# There are too many version to traverse iteratively, just choose the one you like it.
# pre-order: root->left->right
def preorder_traversal_iteratively(self, root: 'TreeNode'):
    if not root:
        return []
    stack = [root]
    while stack:
        root = stack.pop()
        '''
        add current node logic here
        '''
        self.process_logic(root)

        # push right child first because of FILO
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)


# in-order: left->root->right
def inorder_traversal_iteratively(self, root: 'TreeNode'):
    stack = []
    # keep stack empty and compare root too, compatible with edge case: root=None
    while stack or root:
        # push itself and all left children into stack iteratively
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        '''
        add current node logic here
        '''
        self.process_logic(root)

        # point to right child
        root = root.right


# here I choose to not use
# post-order: left->right->root
def postorder_traversal_iteratively(self, root: 'TreeNode'):
    if not root:
        return []
    stack = [root]
    # used to record whether left or right child has been visited
    last = None

    while stack:
        root = stack[-1]
        # if current node has no left right child, or left child or right child has been visited, then process and pop it
        if not root.left and not root.right or last and (root.left == last or root.right == last):
            '''
            add current node logic here
            '''
            self.process_logic(root)

            stack.pop()
            last = root
        # if not, push right and left child in stack
        else:
            # push right first because of FILO
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)


# post-order: left->right->root
# use visit flag
def postorder_traversal_iteratively2(self, root: 'TreeNode'):
    if not root:
        return []
    stack = [root]
    while stack:
        root = stack[-1]
        # use visited attribute to judge whether it has been visited
        if hasattr(root, 'visited'):
            '''
            add current node logic here
            '''
            self.process_logic(root)

            stack.pop()
            del root.visited
        else:
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            root.visited = True


# level-order
def level_order_traversal_iteratively(self, root: 'TreeNode'):
    if not root:
        return []
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            '''
            add current node logic here
            '''
            self.process_logic(cur)

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        '''
        add level logic here if you need
        '''
