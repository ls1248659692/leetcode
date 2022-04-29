class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def sp(s):
            rli =['']
            for c in s:
                if c in ['-','+','*']:
                    rli.append(c)
                    rli.append('')
                else:
                    rli[-1]+=c
            #rli.append('.')
            return rli

        def calc(ls1,ls2,c):
            if c=='+': return [n+m for n in ls1 for m in ls2]
            if c=='-': return [n-m for n in ls1 for m in ls2]
            if c=='*': return [n*m for n in ls1 for m in ls2]

        sl = sp(expression)
        print(sl)

        def dfw(sl):
            r = []
            if not sl:return [0]
            elif len(sl)==1: return [int(sl[0])]
            else:
                for i in range(1,len(sl),2):
                    r+=calc(dfw(sl[:i]),dfw(sl[i+1:]),sl[i])
            return r
        return dfw(sl)

            