# a Linked list is a linear collection of data elements, whose order is not given by their physical placement in memory.
# Instead, each element points to the next.
#
# when operation with linked list, we can choose to change list node or change node value.
# change node value is more easy-understanding, and may need extra space to store.
#
# Time:  O(1) to insert and delete, O(n) to random access
# Space: O(n)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# add dummy node to help flag the head, usually used in head may changed or merging None edge case.
def dummy_node_assist(self, head):
    dummy = ListNode(0)
    cur = dummy.next = head  # or cur = dummy

    while cur:
        '''
        process current node logic 
        '''
        self.process_logic(cur)

    return dummy.next


# another solution is use self.next, more pythonic
def self_assist(self, head):
    pre, pre.next = self, head

    while pre.next:
        '''
        process current node logic 
        '''
        self.process_logic(pre.next)

    return self.next


# add node
def add_node(pre_node, new_node):
    pre_node.next, new_node = new_node, pre_node.next


# delete node
def delete_node(pre_node):
    pre_node.next = pre_node.next.next


# reverse linked list iteratively
def reverse_iteratively(head: ListNode) -> ListNode:
    prev, cur = None, head
    while cur:
        cur.next, cur, prev = prev, cur.next, cur
    return prev


# reverse linked list recursively
def reverse_recursively(head: ListNode) -> ListNode:
    def recursive(cur, pre=None):
        if not cur:
            return pre
        pre, cur.next = cur.next, pre
        return recursive(pre, cur)

    return recursive(head)
