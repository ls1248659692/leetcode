class Solution:
    def reorderSpaces(self, text: str) -> str:
        tli = [el for el in text.split() if el ]
        if len(tli)==1: return tli[0]+ ' '*(text.count(' '))
        sp = ' '*(text.count(' ')//(len(tli)-1))
        leftn = text.count(' ')%(len(tli)-1)
        s = sp.join(tli)+' '*leftn
        print(s)
        return s