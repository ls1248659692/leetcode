class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        lf,bl = [bills[0]],bills
        for i in range(1,len(bl)):
            lf.append(bl[i])
            if bl[i]==10: 
                if 5 in lf: lf.pop(lf.index(5))
                else:return False
            elif bl[i]==20:
                if 5 in lf and 10 in lf: 
                    lf.pop(lf.index(5))
                    lf.pop(lf.index(10))
                elif  lf.count(5)>=3:
                    for j in range(3):lf.pop(lf.index(5))
                else:return False                
        return True