class Solution:
    def addDigits(self, num: int) -> int:
        sn= str(num)
        while len(sn)>1:
            sn = str(sum(int(e)for e in sn))
        return int(sn)