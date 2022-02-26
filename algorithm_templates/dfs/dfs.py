# Deep-first search is traversing or searching tree or graph data structures, including graph-like solution space.
# it starts at the root node and explores as far as possible along each branch before backtracking.
#
# Time:  O(V+E)     V: vertex, E: edges
# Space: O(V)


# recursion version
def dfs_recursively(self, node, visited: set):
    visited.add(node)
    '''
    process current node logic here
    '''
    self.process_logic(node)

    for next_node in node.get_successors():
        if next_node not in visited:
            self.dfs_recursively(next_node, visited)


# iteration version, uncommon
def dfs_iteratively(self, root):
    stack, visited = [root], set()
    while stack:
        node = stack.pop()
        visited.add(node)
        '''
        process current node logic here
        '''
        self.process_logic(node)

        for next_node in node.get_successors():
            if next_node not in visited:
                stack.append(next_node)
