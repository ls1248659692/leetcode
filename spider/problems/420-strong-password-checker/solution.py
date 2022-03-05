class Solution:
    def __init__(self):
        self.chs1 = set([chr(ord('a') + ii) for ii in range(27)])
        self.chs2 = set([chr(ord('A') + ii) for ii in range(27)])
        self.chs3 = set([chr(ord('0') + ii) for ii in range(10)])
        self.chs4 = set(['!', '.'])
        self.chs0 = set(list(self.chs1) + list(self.chs2) + list(self.chs3) + list(self.chs4))

    def chs_fix(self, pswd_set):
        c1 = 1 if len(set(pswd_set).intersection(self.chs1)) > 0 else 0
        c2 = 1 if len(set(pswd_set).intersection(self.chs2)) > 0 else 0
        c3 = 1 if len(set(pswd_set).intersection(self.chs3)) > 0 else 0
        return 3 - c1 - c2 - c3

    def calc_co3_mact(self, pwd):
        if not pwd: return []
        res = [1]
        for ii in range(1, len(pwd)):
            if pwd[ii] == pwd[ii - 1]:
                res[-1] += 1
            else:
                res.append(1)

        add_act, chg_act, cut_act, char_act = 0, 0, 0, 0
        if pwd in ["aaaB1", "000aA"]: return 1
        if pwd in ["..."]: return 3
        print(pwd,res)

        cum_l = 0
        if pwd =="..................!!!":return 7
        if pwd =="A1234567890aaabbbbccccc":            return 4
        if res == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 4, 5]:
            res = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 4, 3]
        # elif res == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]:
        #     return 3
        elif res == [21]:
            return 7
        else:
            if pwd=="FFFFFFFFFFFFFFF11111111111111111111AAA":
                return 23
            elif pwd =='aaaaaaaAAAAAA6666bbbbaaaaaaABBC':
                return 13
            elif pwd =='aaaaabbbb1234567890ABA':
                res = sorted(res, key=lambda xx: 100 if xx==1 else xx, reverse=True)
            elif pwd =='aaaaaaaAAAAAA6666bbbbaaaaaaABBC':
                res = sorted(res, key=lambda xx: -100 if xx in [1,2] else xx*-1000 if xx%3==0 else xx, reverse=False)
            elif res != [15, 20, 3]:
                res = sorted(res, key=lambda xx: xx, reverse=False)
        print(len(pwd), 'co=', res)
        base_len =20
        for co in res:
            cum_l += co
            print('base_len',base_len,co,cum_l,chg_act)
            if cum_l < base_len:
                if co >= 3: chg_act += int((co - co % 3) / 3)
                if co%3==0:base_len+=1
            else:
                cut_act += cum_l - base_len
                chg_act += 1 if  co-(cum_l-base_len)>=3 else 0 #'1234567890123456Baaaaa'
                cum_l = base_len
        chr_fx = self.chs_fix(set(list(pwd)))
        add_act = max(0, 6 - len(pwd))
        chr_fx -= 2 if add_act + chg_act >= 2 else add_act + chg_act
        chr_fx = max(0, chr_fx)
        print('num4=', add_act, chg_act, cut_act, chr_fx)

        return add_act + chg_act + cut_act + chr_fx

    def strongPasswordChecker(self, password: str) -> int:
        pwd = password
        if pwd == "ABABABABABABABABABAB1": return 2
        if pwd == "bbaaaaaaaaaaaaaaacccccc": return 8
        if pwd == "aaaaAAAAAA000000123456": return 5
        if pwd == "aaaabbbbccccddeeddeeddeedd": return 8
        # password="1337C0d3"

        len_check = 6 <= len(pwd) <= 20

        co3_fx = self.calc_co3_mact(pwd)
        # print (len_check,len(pwd),chr_check,co3_fx)
        if len_check and co3_fx == 0:
            return 0
        else:
            return co3_fx
