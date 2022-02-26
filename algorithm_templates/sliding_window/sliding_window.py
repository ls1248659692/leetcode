# Sliding windows code template is most used in substring match or maximum/minimum problems.
# It uses two-pointer as boundary of sliding window to traverse, and use a counter(dict) maintain current state,
# and a count as condition checker, update it when trigger some key changes.
#
# Time:  O(n)
# Space: O(k) k = len(set(p))
from collections import Counter


# s - target sequence, p - pattern or restrict sequence
def sliding_window_template_with_examples(s, p):
    # initialize the hash map here
    # counter is used to record current state, could use defaultdict in some situation, for example, no p restrict
    counter = Counter(p)

    # two pointers, boundary of sliding window
    start, end = 0, 0
    # condition checker, update it when trigger some key changes, init value depend on your situation
    count = 0
    # result, return int(such as max or min) or list(such as all index)
    res = 0

    # loop the source string from begin to end
    while end < len(s):
        counter[s[end]] += 1
        # update count based on some condition
        if counter[s[end]] > 1:
            count += 1
        end += 1

        # count condition here
        while count > 0:
            '''
            update res here if finding minimum
            '''

            # increase start to make it invalid or valid again
            counter[s[start]] -= 1
            # update count based on some condition
            if counter[s[start]] > 0:
                count -= 1
            start += 1

        '''
        update res here if finding maximum
        '''
        res = max(res, end - start)

    return res


# refer to https://leetcode.com/problems/minimum-window-substring/discuss/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems