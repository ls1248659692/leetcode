class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        pm = [2,3,5,7,11,13,17,19,23,29,31]
        cnt =0
        for i in range(left,right+1):
            if str(bin(i))[2:].count('1') in pm:cnt+=1
        return cnt