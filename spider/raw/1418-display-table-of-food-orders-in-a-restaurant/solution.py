class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dic = {}
        for i in orders:
            if i[1] in dic:
                dic[i[1]].append(i[2])
            else:
                dic[i[1]] = [i[2]]
        
        li = [['Table']]
        dishes = set()
        for v in dic.values():
            for i in v:
                dishes.add(i)
        dishes = list(dishes)
        dishes.sort()
        li[0].extend(dishes)
    
        for i in sorted(dic,key = lambda x:int(x)):
            tmp = [i]
            for d in dishes:
                tmp.append(str(dic[i].count(d)))
            li.append(tmp)
        return li