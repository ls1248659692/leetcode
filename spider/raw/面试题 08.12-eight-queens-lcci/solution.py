class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res =[]
        def ck_rule(i,j,ocups):
            for oci,ocj in ocups:
                if oci==i or ocj==j or oci+ocj==i+j or i-oci==j-ocj:return False
            return True

        for i in range(n):
            res0 = res.copy()
            #print('res0=%s len(res0)=%s '%(res0,len(res0)))
            for j in range(n):
                if not res0:
                    res.append([(i,j)])
                else:
                    #print('res0=%s len(res0)=%s'%(res0,len(res0)))
                    for o in range(len(res0)):
                        ocups=res0[o]
                        if ocups and ck_rule(i,j,ocups):
                            res.append(res[o]+[(i,j)])
            res = [el for el in res if len(el)==i+1]

        def qb(i):
            return ''.join(['Q' if m==i else '.' for m in range(n)])
        res = [ [qb(r[1]) for r in re] for re in res  ]
        print(res)
        return res        