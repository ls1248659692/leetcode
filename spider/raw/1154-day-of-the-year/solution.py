class Solution:
    def dayOfYear(self, date: str) -> int:
        yy= date[:4]
        mm=date[5:7]
        dd=date[8:10]
        ry = int(yy)%4==0 and yy!='1900'
        mli=[0,31,28,31,30,31,30, 31,31,30,31,30,31]
        return sum(mli[:int(mm)]) + int(dd) + (1 if mm>='03' and ry else 0)