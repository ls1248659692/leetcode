class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s_list = s1.split(' ') + s2.split(' ')
        return [i for i in s_list if s_list.count(i) == 1]