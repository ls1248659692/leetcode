class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        li = []
        for i in words:
            a = words[:]
            a.remove(i)
            a = ' '.join(a)
            if i in a:
                li.append(i)
        return li