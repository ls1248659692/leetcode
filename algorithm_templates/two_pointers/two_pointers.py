# two pointers scenario, famous applications such as binary search, quick sort and sliding window.

'''
Classification:
1. old & new state: old, new = new, cur_result
2. slow & fast runner: slow-> fast->->
3. left & right boundary or index: left-> <-right
4. p1 & p2 from two sequences: p1-> p2->
5. start & end sliding window boundary: start-> end->
'''


# old & new state: old, new = new, cur_result
def old_new_state(self, seq):
    # initialize state
    old, new = default_val1, default_val2
    for element in seq:
        '''
        process current element with old state
        '''
        old, new = new, self.process_logic(element, old)


# slow & fast runner: slow-> fast->->
def slow_fast_runner(self, seq):
    # initialize slow runner
    slow = seq[0]   # for index: slow = 0
    # fast-runner grows each iteration generally
    for fast in range(seq):     # for index: range(len(seq))
        '''
        slow-runner grows with some restrictions
        '''
        if self.slow_condition(slow):
            slow = slow.next    # for index: slow += 1
        '''
        process logic before or after pointers movement
        '''
        self.process_logic(slow, fast)


# left & right boundary or index: left-> <-right
def left_right_boundary(self, seq):
    left, right = 0, len(seq) - 1
    while left < right:
        '''
        left index moves when satisfy the condition
        '''
        if self.left_condition(left):
            left += 1

        '''
        right index move when satisfy the condition
        '''
        if self.right_condition(right):
            right -= 1

        '''
        process logic before or after pointers movement
        '''
        self.process_logic(left, right)


# p1 & p2 from two sequences: p1-> p2->
def pointers_from_two_seq(self, seq1, seq2):
    # init pointers
    p1, p2 = 0, 0       # or seq1[0], seq2[0]

    # or other condition
    while p1 < len(seq1) and p2 < len(seq2):
        '''
        p1 index moves when satisfy the condition
        '''
        if self.p1_condition(p1):
            p1 += 1         # or p1 = next(seq1)

        '''
        p2 index move when satisfy the condition
        '''
        if self.p2_condition(p2):
            p2 += 1         # or p2 = next(seq2)

        '''
        process logic before or after pointers movement
        '''
        self.process_logic(p1, p2)


# start & end of sliding window: |start-> ... end->|
# more details in sliding windows templates, here is just about two-pointers part
def start_end_sliding_window(self, seq):
    start, end = 0, 0

    while end < len(seq):
        # end grows in the outer loop
        end += 1

        # start grows with some restrict
        while self.start_condition(start):
            '''
            process logic before pointers movement
            '''
            self.process_logic1(start, end)

            # start grows in the inner loop
            start += 1

        '''
        or process logic after pointers movement
        '''
        self.process_logic2(start, end)

