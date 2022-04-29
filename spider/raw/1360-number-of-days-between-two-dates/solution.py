class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def ndays(dt):
            #print(dt,dt[:4],dt[5:7],dt[8:])
            yy= int(dt[:4])
            yydays = (yy-1970)*365
            rn_yd = sum(1 for y in range(1970,yy) if y%4==0 and y!=2100)
            mm = int(dt[5:7])
            mmdays = sum([0,31,28,31,30,31,30,31,31,30,31,30,31][:mm])
            rn_md = 1 if mm>=3 and yy%4==0 and yy!=2100 else 0
            dd = int(dt[8:])
            print(yy,mm,dd,yydays,mmdays,dd, rn_yd, rn_md)
            return yydays + rn_yd + mmdays + rn_md + dd

        return abs(ndays(date2)-ndays(date1))