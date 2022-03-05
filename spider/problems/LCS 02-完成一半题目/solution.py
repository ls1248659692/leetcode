class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        knli = sorted([questions.count(kn) for kn in set(questions)],reverse=True)
        return [i for i in range(1,len(knli)+1) if sum(knli[:i])>=len(questions)//2][0]