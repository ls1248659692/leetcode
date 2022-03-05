class Solution:
    def calculate(self, s: str) -> int:
        sli=[el for el in s.replace(' ','').replace('+',' + ').replace('-',' - ').replace('*',' * ').replace('/',' / ').split() if el]
        #sli0 = list(sli)
        while '*' in sli or '/' in sli:
            for n in range(len(sli)):
                if sli[n] in ('*','/'):
                    sli[n-1] = str(int(sli[n-1]) *int(sli[n+1]) if sli[n]=='*' else int(sli[n-1]) //int(sli[n+1]))
                    sli[n],sli[n+1] ='','' 
                    break               
            sli = [el for el in sli if el]
            
        sstr= ''.join(sli).replace('-','+-')
        ssli = sstr.split('+')
        return sum(int(el) for el in ssli)

        while '+' in sli or '-' in sli:
            for n in range(len(sli)):
                if sli[n] in ('+','-'):
                    sli[n-1] = str(int(sli[n-1]) +int(sli[n+1]) if sli[n]=='+' else int(sli[n-1]) -int(sli[n+1]))
                    sli[n],sli[n+1] ='',''
                    break
            sli = [el for el in sli if el]
        print(''.join(sli))
        return int(''.join(sli))
        #return eval(s.replace('/','//'))