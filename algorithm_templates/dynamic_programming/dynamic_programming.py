# simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner
# dynamic programming = recursion + memorized
# state definition, state transition equation, optimal substructure
# direction: bottom-up or top-down


def dynamic_programming_template_with_example(word1, word2):
    m, n = len(word1), len(word2)

    # states definition: cur_min_edit_dist
    # states compressed to two states: old and new
    dp = [[0] * (m + 1) for _ in range(2)]

    # initialize the initial edit distance, add one more state for init state
    for i in range(0, m + 1):
        dp[0][i] = i

    cur = 1
    for i in range(n):
        # initialize the init state
        dp[cur][0] = i + 1
        for j in range(m):
            # state transition equation
            # if char matched, this is the min dist.
            if word1[j] == word2[i]:
                dp[cur][j + 1] = dp[cur ^ 1][j]
            # otherwise, 1 + minimum of edit/remove/add operations
            else:
                dp[cur][j + 1] = 1 + min(dp[cur ^ 1][j], dp[cur ^ 1][j + 1], dp[cur][j])
        # switch between two states
        cur ^= 1
    # return the last state as result
    return dp[cur ^ 1][-1]
