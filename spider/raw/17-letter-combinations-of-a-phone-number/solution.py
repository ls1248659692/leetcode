class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:return []
        tdic={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        dic = {kk:list(tdic[kk])for kk in tdic}
        print(dic)
        d_li = [dic[int(dd)]for dd in digits]
        t_li=d_li[0]
        for ii in range(1,len(d_li)):
            tmp_li = []
            for jj in range(len(d_li[ii])):
                tmp_li += [el +d_li[ii][jj] for el in t_li]
            t_li = tmp_li
        return t_li