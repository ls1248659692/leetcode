class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # bt = ''.join([str(e) for e in bits])
        # while len(bt)>=2:
        #     if bt[0]=='0':bt=bt[1:]
        #     else:bt= bt[2:]
        # return bt=='0'
        # print(bt)
        cnt = 0
        for i in range(len(bits)-2,-1,-1):
            if bits[i]==0:
                break
            cnt+=1
        return cnt%2==0