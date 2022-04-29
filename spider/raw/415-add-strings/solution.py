class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        mt = max(len(num1),len(num2))+1
        num1,num2,r = list('0'*(mt-len(num1)) + num1),list('0'*(mt-len(num2)) + num2),['0' for i in range(mt)]
        #print(num1,num2,r)
        for i in range(1,mt):
            su = int(num1[-i])+int(num2[-i])+int(r[-i])
            
            r[-i]= str(su%10)
            r[-i-1]=str(su//10)
            #print(r,str(su%10))
        #print(r)
        res = ''.join(r)
        while len(res)>1 and res[0]=='0':res=res[1:]
        return res