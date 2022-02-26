# divide and conquer is an algorithm design paradigm based on multi-branched recursion. A divide-and-conquer
# algorithm works by recursively breaking down a problem into two or more sub-problems of the same or related type,
#  until these become simple enough to be solved directly. The solutions to the sub-problems are then combined to
# give a solution to the original problem.
#
# ideal for parallel computing, no duplicate sub-questions(intermediate results)
# divide & conquer vs. dynamic processing or memory caches
# similar to map reduce


def divide_conquer(self, problem, *params):
    # recursion terminator
    if problem is None:
        # terminator logic here
        return self.process_terminator_logic()

    # prepare data
    data = self.prepare_data(problem)

    # divide the problem to sub-problems
    sub_problems = self.split_problem(problem, data)

    results = []
    # conquer sub problems
    for sub_problem in sub_problems:
        results += self.divide_conquer(sub_problem, params)

    # process and generate the final result
    result = self.merge_results(results)

    return result
