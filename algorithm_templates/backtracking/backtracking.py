# Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably
#  constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate
#  ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
#
# backtracking vs. dfs
# traverse in solution space vs. traverse in data structure space, pruned of dfs


def backtracking(self, data, candidate):
    # pruning
    if self.reject(data, candidate):
        return

    # reach the end
    if self.accept(data, candidate):
        return self.output(data, candidate)

    # drill down
    for cur_candidate in self.all_extension(data, candidate):
        # or you can choose to prune here, recursion depth - 1
        if not self.should_to_be_pruned(cur_candidate):
            self.backtracking(data, cur_candidate)



