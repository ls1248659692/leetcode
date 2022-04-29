class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        cont = cont[::-1]
        fz,fm =cont[0],1

        for i in range(1,len(cont)):
            fz,fm = fm,fz
            fz,fm = cont[i]*fm+fz,fm
        return [fz,fm]
