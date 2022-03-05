class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        lst = []
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    lst.append([i,j])
        dic= {}
        for b,a in lst:
            dic.setdefault(b,[]).append(a)
        td={}
        for b in dic:
            aset,tset =set(dic[b]),set(dic[b])
            while aset:
                _aset,aset=set(aset),set()
                for bb in _aset:
                    for aa in dic.get(bb,set()):
                        if aa not in tset:
                            aset.add(aa)
                for p in aset:tset.add(p)
            td[b]=tset
        # it = sorted(td.items(),key=lambda x:len(x[1]))
        res = []
        for i in td.values():
            if i not in res:res.append(i)
        return len(res)