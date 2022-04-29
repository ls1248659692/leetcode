class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime_num = 0
        prime_com = 1
        non_com = 1
        nli=[2,3,5,7,11,13,]
        nli=[]
        for i in range(2,n+1):
            isp=True
            for j in range(2,int(n**0.5)+1):
                if i%j==0 and i!=j:
                    isp=False
            if isp:nli.append(i)
        prime_num=len(nli)
        print(nli)

        ex_num = n - prime_num
        for i in range(1,prime_num+1):
            prime_com = prime_com * i
        for j in range(1,ex_num +1):
            non_com = non_com * j
        return (non_com * prime_com)%(10**9 +7)