class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        else:
            cn_1 = self.countAndSay(n-1)
            dli = [[cn_1[0],1]]
            for ii in range(1,len(cn_1)):
                if cn_1[ii]==cn_1[ii-1]:
                    dli[-1][-1] +=1
                else:
                    dli.append([cn_1[ii],1])
            print ('n=%s,dli=%s'%(n,dli))
            return ''.join([str(el[1])+el[0] for el in dli])