class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l1=[]
        l2=[]
        for l in logs:
            if l[-1].isalpha():
                l1.append(l)
            else:
                l2.append(l)
        l1.sort(key=lambda x:(x[x.index(' ')+1:],x[:x.index(' ')+1]))
        return l1+l2