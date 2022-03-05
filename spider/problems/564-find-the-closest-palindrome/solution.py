class Solution:
    def nearestPalindromic(self, n: str) -> str:
        ll, intn = len(n), int(n)
        if ll == 1: return str(intn - 1)
        candlist = [int('9'*(ll-1) if (ll-1) else '0'), int('1'+'0'*(ll-1)+'1'), int(n[:ll // 2] + n[(ll - 1) // 2::-1])]
        halfn = int(n[:(ll + 1) // 2])
        candlist += [int(str(halfn - 1) + str(halfn - 1)[- 1 - ll % 2::-1])] if halfn != 10 ** ((ll - 1) // 2) else []
        candlist += [int(str(halfn + 1) + str(halfn + 1)[- 1 - ll % 2::-1])] if str(halfn) != '9' * ((ll + 1) // 2 + 1) else []
        candlist.sort()
        return str([cc for cc in candlist if abs(cc - intn) == min([abs(cc - intn) for cc in candlist if abs(cc - intn) != 0])][0])