class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ma = a if len(a) > len(b) else b
        mi = b if len(a) > len(b) else a
        mi = '0' * (len(ma) - len(mi)) + mi
        tli = ['0' for i in range(len(ma) + 1)]
        for i in range(1, len(mi) + 1):
            su = sum([int(mi[-i]), int(ma[-i]), int(tli[-i])])
            tli[-i] = str(su % 2)
            tli[-i - 1] = str(su // 2)
        r = (''.join(tli))
        if not r: return ''
        while len(r) > 1 and r[0] == '0': r = r[1:]
        return r        