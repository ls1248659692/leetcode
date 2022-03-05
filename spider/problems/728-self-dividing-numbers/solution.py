class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r =[]
        for i in range(left,right+1):
            digs = [int(e) for e in str(i)]
            if 0 in digs:continue
            if sum(i%d!=0 for d in digs)==0:r.append(i)
        return r