# Breadth-first search is traversing or searching tree or graph data structures, including graph-like solution space.
# it explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
#
# Time:  O(V+E)     V: vertex, E: edges
# Space: O(V)
from collections import deque


# iteration version, using deque
def bfs_iteratively_by_queue(self, start, target=None):
    queue, visited = deque([start]), {start}

    while queue:
        node = queue.popleft()
        visited.add(node)
        '''
        process current node logic here
        '''
        self.process_logic(node)

        # target is optional
        if node == target:
            '''
            reach the goal and break out
            '''
            self.process_target_logic(target)
            break
        for next_node in node.get_successors():
            if next_node not in visited:
                queue.append(next_node)


# iteration version, using list, pythonic-style
# conciser but more memory, mainly used when you want to collect the whole list
def bfs_iteratively_by_list(self, start, target=None):
    node_list, visited = [start], {start}

    # append while traversing
    for node in node_list:
        visited.add(node)
        '''
        process current node logic here
        '''
        self.process_logic(node)

        # target is optional
        if node == target:
            '''
            reach the goal and break out
            '''
            self.process_target_logic(target)
            break
        for next_node in node.get_successors():
            if next_node not in visited:
                node_list += node

    # basically the node_list is useful here
    return node_list


# recursion version, uncommon
def bfs_recursively(self, queue: deque, visited: set, target=None):
    if not queue:
        return

    node = queue.popleft()
    visited.add(node)
    '''
    process current node logic here
    '''
    self.process_logic(node)

    # target is optional
    if node == target:
        '''
        reach the goal and break out
        '''
        self.process_target_logic(target)
        return
    for next_node in node.get_successors():
        if next_node not in visited:
            queue.append(next_node)
    self.bfs_recursively(queue, visited)


# bfs list comprehension in row of binary tree
def bfs_row(self, root):
    row = [root]
    while row:
        '''
        process current node logic here
        '''
        # process logic separately
        row = [child for node in row for child in (node.left, node.right) if node]