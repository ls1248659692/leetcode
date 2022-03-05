class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:return [[1]]
        elif numRows==2:return [[1],[1,1]]
        else:
            res = self.generate(numRows-1)
            res.append([1]+ [res[-1][i]+res[-1][i+1] for i in range(numRows-2)]+[1])
            return res