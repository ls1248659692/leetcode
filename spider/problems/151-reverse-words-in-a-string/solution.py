class Solution:
    def reverseWords(self, s: str) -> str:
        tli = [el for el in s.strip().split() if el]
        return ' '.join([tli[ii] for ii in range(len(tli)-1,-1,-1)])