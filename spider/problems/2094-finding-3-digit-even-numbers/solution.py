class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def pem_v0(digits):
            res =set()
            for i in range(len(digits)):
                if digits[i] not in [0,2,4,6,8]:continue
                for j in range(len(digits)):
                    if i==j:continue
                    for k in range(len(digits)):
                        if k in[i,j] or digits[k]==0:continue
                        res.add(digits[k]*100+digits[j]*10+digits[i])
            return sorted(list(res))

        def perm_v1(digits):
            res = [[digits[i],[i]] for i in range(len(digits))]
            dic = {}
            for dd in range(1,3):    
                res0 = res.copy()
                for i in range(len(digits)):
                    dv =10**dd *digits[i]
                    for vv,pos in res0:
                        if len(pos)==dd and (i not in pos) and dv+vv>=(100 if dd==2 else 0) and (dv+vv not in dic) and (dv+vv)%2==0:
                            dic.setdefault(dv+vv,0)
                            res.append([dv+vv,pos+[i]])
                print(len(res))
            return sorted([el for el in list(dic.keys()) if el>=100 and el%2==0])

        return perm_v1(digits)
        