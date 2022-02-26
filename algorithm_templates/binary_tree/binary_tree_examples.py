from collections import defaultdict
from collections import deque


# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
binary tree examples
'''


# [101] https://leetcode.com/problems/symmetric-tree/
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
def isSymmetric(root):
    def isSymmetricR(left, right):
        if left and right:
            return left.val == right.val and isSymmetricR(left.left, right.right) and isSymmetricR(
                left.right, right.left)
        return left is right

    return isSymmetricR(root, root)


# [105] https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Given preorder and inorder traversal of a tree, construct the binary tree.
def buildTree(preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
    if not preorder:
        return
    index = inorder.index(preorder[0])
    root = TreeNode(preorder[0])
    root.left = buildTree(preorder[1:index + 1], inorder[0:index])
    root.right = buildTree(preorder[index + 1:], inorder[index + 1:])
    return root


# [110] https://leetcode.com/problems/balanced-binary-tree/
# Given a binary tree, determine if it is height-balanced.
def isBalanced(root):
    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1
        return 1 + max(left, right)

    if not root:
        return True
    return dfs(root) != -1


# [100] https://leetcode.com/problems/same-tree/discuss/32729/Shortest%2Bsimplest-Python
# check if they are the same or not
#
# proper way
def isSameTree1(p, q):
    if p and q:
        return p.val == q.val and isSameTree1(p.left, q.left) and isSameTree1(p.right, q.right)
    return p is q


# tuplify way:
def isSameTree2(p, q):
    def t(n):
        return n and (n.val, t(n.left), t(n.right))

    return t(p) == t(q)


# map way
def isSameTree3(p, q):
    return p and q and p.val == q.val and all(map(isSameTree3, (p.left, p.right), (q.left, q.right))) or p is q


# [314] https://leetcode.com/problems/binary-tree-vertical-order-traversal
# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
#
# BFS
def verticalOrder(root: 'TreeNode') -> 'List[List[int]]':
    if not root:
        return []

    vertical_dict = defaultdict(list)
    queue = [(root, 0)]

    for root, vertical_idx in queue:
        vertical_dict[vertical_idx].append(root.val)
        if root.left:
            queue.append((root.left, vertical_idx - 1))
        if root.right:
            queue.append((root.right, vertical_idx + 1))

    res = []
    for key in sorted(vertical_dict.keys()):
        res += [vertical_dict[key]]

    return res


# [116] https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# populate each next pointer to point to its next right node
def connect(root: 'Node') -> 'Node':
    # connect left child to right child, and cross connect left right child to right left child in recursion
    def connect_inner(l, r):
        if not l.left or not r.right:
            return
        l.left.right = l.right
        l.right.next = r.left
        r.left.next = r.right

        connect_inner(l.left, l.right)
        connect_inner(l.right, r.left)
        connect_inner(r.left, r.right)

    if not root or root.left:
        return root
    root.left.next = root.right
    connect_inner(root.left, root.right)
    return root


# [226] https://leetcode.com/problems/invert-binary-tree/
# Invert a binary tree
#
# recursively
def invertTree1(root):
    if root:
        root.left, root.right = invertTree1(root.right), invertTree1(root.left)
        return root


# [226] https://leetcode.com/problems/invert-binary-tree/
# Invert a binary tree
#
# BFS
def invertTree2(root: 'TreeNode') -> 'TreeNode':
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            # accept add None node to queue, in order to deal with edge case together
            queue.append(node.left)
            queue.append(node.right)
    return root


# [226] https://leetcode.com/problems/invert-binary-tree/
# Invert a binary tree
#
# DFS
def invertTree3(root: 'TreeNode') -> 'TreeNode':
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            # accept push None node to stack, in order to deal with edge case together
            stack.append(node.left)
            stack.append(node.right)
    return root


# [235] https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# find the lowest common ancestor (LCA) of two given nodes in the BST.
def lowestCommonAncestor(root, p, q):
    while (root.val - p.val) * (root.val - q.val) > 0:
        root = (root.left, root.right)[p.val > root.val]
    return root


# [236] https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# find the lowest common ancestor (LCA) of two given nodes in binary tree
#
# recursively
def lowestCommonAncestor1(root, p, q):
    if root in (None, p, q): return root
    left, right = (lowestCommonAncestor1(kid, p, q)
                   for kid in (root.left, root.right))
    return root if left and right else left or right


# [236] https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# find the lowest common ancestor (LCA) of two given nodes in binary tree
#
# iteratively, use common path, find first intersection point
def lowestCommonAncestor2(root, p, q):
    def path(root, goal):
        path, stack = [], [root]
        while True:
            node = stack.pop()
            if node:
                if node not in path[-1:]:
                    path += node,
                    if node == goal:
                        return path
                    stack += node, node.right, node.left
                else:
                    path.pop()

    return next(a for a, b in zip(path(root, p), path(root, q))[::-1] if a == b)


# [545] https://leetcode.com/problems/boundary-of-binary-tree
# Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root.
# Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes
# Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node.
# If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary.
def boundaryOfBinaryTree(root):
    res = []

    def preorder(node, is_left, is_right):
        if not node:
            return
        is_leaf_or_left = (not node.left and not node.right) or is_left
        # append leaf or left boundary
        if is_leaf_or_left:
            res.append(node.val)
        # pre-order traversal
        if not node.left and not node.right:
            return
        elif not node.right:
            preorder(node.left, is_left, is_right and not is_left)
        elif not node.left:
            preorder(node.right, is_left and not is_right, is_right)
        else:
            preorder(node.left, is_left, False)
            preorder(node.right, False, is_right)
        # append right boundary, in backtrack so don't need reverse order
        if is_right and not is_leaf_or_left:
            res.append(node.val)

    preorder(root, True, True)
    return res


'''
binary search tree examples
'''


# [270] https://leetcode.com/problems/closest-binary-search-tree-value/
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
#
# recursively
def closestValue1(root: 'TreeNode', target: float) -> int:
    def dfs(root, diff, closest):
        if abs(target - root.val) < diff:
            diff = abs(target - root.val)
            closest = root.val
        if root.val > target and root.left:
            return dfs(root.left, diff, closest)
        elif root.val < target and root.right:
            return dfs(root.right, diff, closest)
        return closest

    return dfs(root, float('inf'), None)


# [270] https://leetcode.com/problems/closest-binary-search-tree-value/
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
#
# iteratively
def closestValue(root: 'TreeNode', target: float) -> int:
    diff, closest = float('inf'), None
    while root:
        if abs(target - root.val) < diff:
            diff = abs(target - root.val)
            closest = root.val
        if root.val > target:
            root = root.left
        else:
            root = root.right
    return closest


# [098] https://leetcode.com/problems/validate-binary-search-tree/
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# in-order traversal iteratively
def isValidBST1(root: 'TreeNode') -> 'bool':
    stack, inorder = [], float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        # If next element in inorder traversal is smaller than the previous one, that's not BST.
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right
    return True


# [098] https://leetcode.com/problems/validate-binary-search-tree/
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# DFS，use parameter or return value
def isValidBST2(root: 'TreeNode') -> 'bool':
    if not root:
        return True

    def isBSTHelper(node, lower_limit, upper_limit):
        if lower_limit is not None and node.val <= lower_limit:
            return False
        if upper_limit is not None and upper_limit <= node.val:
            return False

        left = isBSTHelper(node.left, lower_limit, node.val) if node.left else True
        if left:
            right = isBSTHelper(node.right, node.val, upper_limit) if node.right else True
            return right
        else:
            return False

    return isBSTHelper(root, None, None)


# [098] https://leetcode.com/problems/validate-binary-search-tree/
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# BFS
def isValidBST3(root: 'TreeNode') -> 'bool':
    if not root:
        return True

    stack = [(root, None, None), ]
    while stack:
        root, lower_limit, upper_limit = stack.pop()
        if root.right:
            if root.right.val > root.val:
                if upper_limit and root.right.val >= upper_limit:
                    return False
                stack.append((root.right, root.val, upper_limit))
            else:
                return False
        if root.left:
            if root.left.val < root.val:
                if lower_limit and root.left.val <= lower_limit:
                    return False
                stack.append((root.left, lower_limit, root.val))
            else:
                return False
    return True


# [285] https://leetcode.com/problems/inorder-successor-in-bst/
# find the in-order successor of that node in the BST
#
# iteratively
def inorderSuccessor(root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    # if has right child, get left-most leaf directly
    if p.right:
        p = p.right
        while p.left:
            p = p.left
        return p
    else:
        # use in-order traversal
        stack, find = [], False
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if find:
                return root
            if root == p:
                find = True
            root = root.right
    if find:
        return None


# [285] https://leetcode.com/problems/inorder-successor-in-bst/
# find the in-order successor of that node in the BST
#
# recursively
def inorderSuccessor(root, p):
    res = None

    def dfs(root, p):
        nonlocal res
        if not root:
            return
        if p.val < root.val:
            res = root
            dfs(root.left, p)
        else:
            dfs(root.right, p)

    dfs(root, p)
    return res


# [669] https://leetcode.com/problems/trim-a-binary-search-tree/
# trim the tree so that all its elements lies in [L, R]
#
# recursively
def trimBST(self, root: 'TreeNode', L: int, R: int) -> 'TreeNode':
    if not root:
        return
    if root.val < L:
        return self.trimBST(root.right, L, R)
    elif root.val > R:
        return self.trimBST(root.left, L, R)
    else:
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root


# [426] https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list
# convert bst to sorted doubly linked list
#
# in-order traversal iteratively
def treeToDoublyList(root: 'Node') -> 'Node':
    if not root:
        return None
    pre = dummy = TreeNode(0, None, None)
    cur, stack = root, []
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        pre.right, cur.left, pre = cur, pre, cur
        cur = cur.right
    pre.right, dummy.right.left = dummy.right, pre
    return dummy.right
