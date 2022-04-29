class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        start = [1,2,1]
        for j in range(2,rowIndex):
            temp = []
            for i in range(1,len(start)):
                temp = temp + [start[i] + start[i-1]]
            start = [1] + temp + [1]
        return(start)