class Solution:
    def calPoints(self, ops: List[str]) -> int:
        sli =[]
        for op in ops:
            if op.isdigit() or (op[0]=='-' and op[1:].isdigit):sli.append(int(op))
            elif op=='+':sli.append(sli[-1]+sli[-2])
            elif op=='D':sli.append(sli[-1]*2)
            elif op=='C':sli.pop()
            #print(sli)
        #print(sli)
        return sum(sli)