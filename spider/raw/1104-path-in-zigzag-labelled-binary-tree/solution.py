class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        lb = label
        tli =[lb]
        while lb>1:
            po = int(math.log2(lb))
            lb = [i for i in range(2**(po-1),2**po)][(2**po-lb-1)//2]
            tli.append(lb)
        print(tli)
        return tli[::-1]