# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# [237] https://leetcode.com/problems/delete-node-in-a-linked-list/
# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
#
# change value
def deleteNode(node: ListNode):
    # doesn't work, if node is tail
    node.val, node.next = node.next.val, node.next.next


# [2] https://leetcode.com/problems/add-two-numbers/
# Add the two numbers and return it as a linked list.
#
# simulation
def addTwoNumbers1(l1, l2):
    addends = l1, l2
    dummy = end = ListNode(0)
    carry = 0
    while addends or carry:
        carry += sum(a.val for a in addends)
        addends = [a.next for a in addends if a.next]
        end.next = end = ListNode(carry % 10)
        carry /= 10
    return dummy.next


# [2] https://leetcode.com/problems/add-two-numbers/
# Add the two numbers and return it as a linked list.
#
# convert to int
def addTwoNumbers2(l1, l2):
    def toint(node):
        return node.val + 10 * toint(node.next) if node else 0

    def tolist(n):
        node = ListNode(n % 10)
        if n > 9:
            node.next = tolist(n / 10)
        return node

    return tolist(toint(l1) + toint(l2))


# [21] https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a new list.
#
# iteratively
def mergeTwoLists1(l1: ListNode, l2: ListNode) -> ListNode:
    curr = dummy = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next


# [21] https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a new list.
#
# recursively
# first make sure a starts smaller, use its head as result, and merge the remainders behind it.
def mergeTwoLists2(a, b):
    if a and b:
        if a.val > b.val:
            a, b = b, a
        a.next = mergeTwoLists2(a.next, b)
    return a or b


# [21] https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a new list.
#
# recursively
# make sure that a is the "better" one (meaning b is None or has larger/equal value). Then merge the remainders behind a.
def mergeTwoLists3(a, b):
    if not a or b and a.val > b.val:
        a, b = b, a
    if a:
        a.next = mergeTwoLists3(a.next, b)
    return a


# [24] https://leetcode.com/problems/swap-nodes-in-pairs/
# Given a linked list, swap every two adjacent nodes and return its head.
#
# Since the head doesn't have a previous node, I just use self instead.
# To go from "pre -> a -> b -> b.next" to "pre -> b -> a -> b.next", we need to change those three references.
# Instead of thinking about in what order I change them, I just change all three at once.
def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next


# [234] https://leetcode.com/problems/palindrome-linked-list/
# Given a singly linked list, determine if it is a palindrome.
def isPalindrome(head: ListNode) -> bool:
    check = None
    slow = fast = head
    # traverse and reverse first half link list at the same time
    while fast and fast.next:
        fast = fast.next.next
        check, check.next, slow = slow, check, slow.next

    # solve odd and even problem
    if fast:
        slow = slow.next
    while slow and slow.val == check.val:
        slow = slow.next
        check = check.next
    # check whether reach the end
    return not check


# [82] https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# change node
def deleteDuplicates1(head: ListNode) -> ListNode:
    dummy = pre = ListNode(0)
    dummy.next = head
    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            pre.next = head
        else:
            pre = pre.next
            head = head.next
    return dummy.next


# [82] https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# change value
def deleteDuplicates2(head: ListNode) -> ListNode:
    dummy = ListNode(float('inf'))
    cur = dummy.next = head
    res, duplicated = [dummy.val], False
    while cur:
        if res[-1] == cur.val:
            duplicated = True
        else:
            if duplicated:
                res[-1] = cur.val
            else:
                res.append(cur.val)
            duplicated = False
        cur = cur.next
    if duplicated:
        res.pop()
    cur = dummy
    for v in res[1:]:
        cur.next.val = v
        cur = cur.next
    cur.next = None
    return dummy.next


# [25] https://leetcode.com/problems/reverse-nodes-in-k-group/
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# iteratively
def reverseKGroup1(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    dummy = jump = ListNode(0)
    dummy.next = l = r = head

    while True:
        count = 0
        while r and count < k:  # use r to locate the range
            r = r.next
            count += 1
        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):  # do it k times
                cur.next, cur, pre = pre, cur.next, cur  # standard reversing
            jump.next, jump, l = pre, l, r  # connect two k-groups
        else:
            return dummy.next


# [25] https://leetcode.com/problems/reverse-nodes-in-k-group/
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# recursively
def reverseKGroup2(head, k):
    l, cur = 0, head
    while cur:
        l += 1
        cur = cur.next
    if k <= 1 or l < k:
        return head
    pre, cur = None, head
    for _ in range(k):
        post = cur.next
        cur.next, pre, cur = pre, cur, post
    head.next = reverseKGroup2(cur, k)
    return pre


# [142] https://leetcode.com/problems/linked-list-cycle-ii/
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:  # reach the end, means no cycle
        return None
    while head != slow:
        slow = slow.next
        head = head.next
    return head


# [146] https://leetcode.com/problems/lru-cache/
# Design and implement a data structure for Least Recently Used (LRU) cache.
#
# double linked node, or can use OrderedDict in collection
class DLinkedNode:
    def __init__(self, key, val):
        self.pre = None
        self.next = None
        self.key = key
        self.val = val


class DLinkedList:
    def __init__(self):
        self.head = DLinkedNode(0, 0)
        self.tail = DLinkedNode(0, 0)
        self.__add(self.head, self.tail)
        self.count = 0

    def remove(self, node):
        node.pre.next, node.next.pre = node.next, node.pre
        self.count -= 1

    @staticmethod
    def __add(node1, node2):
        node1.next, node2.pre = node2, node1

    def push(self, node):
        self.__add(self.tail.pre, node)
        self.__add(node, self.tail)
        self.count += 1

    def pop(self):
        first = self.head.next
        self.__add(self.head, self.head.next.next)
        self.count -= 1
        return first

    def __len__(self):
        return self.count


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = DLinkedList()
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.queue.remove(node)
            self.queue.push(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.queue.remove(node)
            self.queue.push(node)
        else:
            if len(self.queue) == self.capacity:
                del self.dict[self.queue.pop().key]
            node = DLinkedNode(key, value)
            self.dict[key] = node
            self.queue.push(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
