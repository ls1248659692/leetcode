class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dic={'(':0,')':0}
        tli =['(']
        for ii in range(1,n*2):
            tmpli=[]
            tmpli += [el+'(' for el in tli if el.count('(')<n]
            tmpli += [el+')' for el in tli if el.count('(')-el.count(')')>0]
            tli = tmpli
            print(tli)
        return tli