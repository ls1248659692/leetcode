class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def zdgys(a,b):
            if a % b == 0:return b
            else: return zdgys(b,a%b)
        li = []
        for i in range(1,n+1):
            for k in range(1,i):
                if zdgys(k,i) == 1:li.append('{}/{}'.format(k,i))
        return li

        # one line probability
