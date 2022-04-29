class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # i, res = 0, 0
        # while truckSize >0 and i<len(boxTypes):
        #     if truckSize > boxTypes[i][0]:
        #         res += boxTypes[i][0]*boxTypes[i][1]
        #         truckSize -= boxTypes[i][0]
        #     else:
        #         res += truckSize*boxTypes[i][1]
        #         truckSize = 0
        #     i += 1
        # return res
        boxTypes.sort(key = lambda x:x[1],reverse = True)
        sz,un=0,0
        for i in range(len(boxTypes)):
            sz,un = sz+min(truckSize-sz,boxTypes[i][0]),un+min(truckSize-sz,boxTypes[i][0])*boxTypes[i][1]
        return un