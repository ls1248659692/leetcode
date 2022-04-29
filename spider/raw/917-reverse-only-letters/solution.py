class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        sli = list(s)
        tli =[i for i in range(len(s)) if s[i].isalpha()]
        for i in range(1,len(tli)//2+1):
            sli[tli[i-1]], sli[tli[-i]]= sli[tli[-i]],sli[tli[i-1]]
        return ''.join(sli)
