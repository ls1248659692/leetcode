# Recursion is a common method of simplification is to divide a problem into subproblems of the same type.


# param such as current path, result, visited set
def recursion(self, level, *params):
    # recursion terminator
    if level > self.MAX_LEVEL:
        '''
        terminator logic here
        '''
        self.process_teminator_logic()
        return

    '''
    process logic in current level, such as update state (params)
    '''
    self.process_logic(level)
    self.update_status(params)

    # drill down
    self.recursion(level + 1, params)

    '''
    reverse the current level status if needed, such as revert the params (opposite operation of upper code block) 
    '''
    self.revert_status(params)


# interval merge
# definition: interval = [start, end]
def add_interval(new_interval, intervals):
    if intervals and intervals[-1][1] >= new_interval[0]:
        if intervals[-1][1] < new_interval[1]:
            intervals[-1][1] = new_interval[1]
    else:
        intervals.append(new_interval)
