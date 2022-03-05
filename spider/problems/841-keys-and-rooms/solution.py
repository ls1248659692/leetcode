class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if rooms[0] == []:return False
        lst = []
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                lst.append([i,rooms[i][j]])
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
            td[b]=tset |set([b])
        print(td)
        # print(td[0])
        return len(td[0])==len(rooms)