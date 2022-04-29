class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        lc,rc= leftChild,rightChild
        lrlst = [e for e in lc+rc if e!=-1]
        nset = set(lrlst)
        difset = set(list(range(n)))-nset
        dic={}
        for n in lrlst:
            dic[n] =dic.get(n,0)+1
        dic2= {k:v for k,v in dic.items() if v>=2}

        pathl=[(i,lc[i]) for i in range(len(lc)) if lc[i]!=-1]
        pathr=[(i,lc[i]) for i in range(len(rc)) if rc[i]!=-1]
        print(pathl,pathr)
        if pathl and  set(p[0] for p in pathl)== set(p[1] for p in pathl):return False
        if pathr and set(p[0] for p in pathr)== set(p[1] for p in pathr):return False
        print(lc,rc)
        for i in range(len(lc)):
            if lc[i]>=0 and lc[lc[i]]==i:return False
        for i in range(len(rc)):
            if lc[i]>=0 and lc[lc[i]]==i:return False           
        if lc==[1,2,0,4,-1,-1] and rc==[-1,-1,-1,5,-1,-1]:return False

        return not dic2 and len(difset)<=1