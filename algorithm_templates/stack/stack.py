# stack common operation: push, pop, top
# stack is used in pairs, maintain extreme value
#
# FILO: First In, Last Out
# Time:  O(1)
# Space: O(n)


# sequence stack based on list
def stack_operations():
    # initialization
    stack = []

    # size of stack
    size = len(stack)

    # push
    stack.append(1)

    # check is empty
    if stack:
        # top
        top = stack[-1]

        # pop
        stack.pop()

